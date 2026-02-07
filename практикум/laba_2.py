import logging
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Application, CommandHandler, MessageHandler, filters,
    ContextTypes, ConversationHandler
)
from config import BOT_TOKEN

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Состояния диалога
ADDING_HABIT, DELETING_HABIT = range(2)

# Хранилище данных пользователей
user_data = {}

# Кнопки
main_keyboard = ReplyKeyboardMarkup([
    ["📋 Мои привычки", "✚ Добавить привычку"],
    ["❌ Удалить привычку", "📊 Статистика"],
    ["🏆 Челленджи", "🥇 Достижения"],
    ["🌍 Рейтинг", "ℹ️ Помощь"]
], resize_keyboard=True)

# --- Проверка достижений ---
def check_achievements(uid):
    u = user_data[uid]
    unlocked = []

    if "Первый шаг" not in u["achievements"] and len(u["habits"]) >= 1:
        u["achievements"].append("Первый шаг")
        unlocked.append("🎯 Первый шаг — вы добавили первую привычку!")

    if "Уверенный старт" not in u["achievements"] and u["completed"] >= 10:
        u["achievements"].append("Уверенный старт")
        unlocked.append("💪 Уверенный старт — выполнено 10 привычек!")

    if "Железная воля" not in u["achievements"] and u["completed"] >= 50:
        u["achievements"].append("Железная воля")
        unlocked.append("🔥 Железная воля — выполнено 50 привычек!")

    if "Настоящий мастер" not in u["achievements"] and u["level"] >= 5:
        u["achievements"].append("Настоящий мастер")
        unlocked.append("⭐ Настоящий мастер — вы достигли 5 уровня!")

    return unlocked

# --- Основные команды ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    uid = user.id
    if uid not in user_data:
        user_data[uid] = {
            "habits": {}, "points": 0, "level": 1,
            "completed": 0, "achievements": []
        }
    await update.message.reply_text(
        f"Привет, {user.first_name}! 🌱\n"
        f"Я — твой трекер привычек. Выбирай действие:",
        reply_markup=main_keyboard
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💡 Возможности бота:\n"
        "• Добавляй привычки и отмечай выполнение.\n"
        "• Получай очки, уровни и достижения.\n"
        "• Участвуй в челленджах.\n"
        "• Смотри рейтинг и достижения других игроков."
    )

# --- Добавление привычек ---
async def add_habit_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Введите название новой привычки:")
    return ADDING_HABIT

async def add_habit_save(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid = update.effective_user.id
    habit = update.message.text.strip()
    if not habit:
        await update.message.reply_text("Название не может быть пустым.")
        return ADDING_HABIT

    user_data[uid]["habits"][habit] = 0
    msg = f"Привычка «{habit}» добавлена ✅"
    achievements = check_achievements(uid)
    if achievements:
        msg += "\n\n" + "\n".join(achievements)
    await update.message.reply_text(msg, reply_markup=main_keyboard)
    return ConversationHandler.END

# --- Удаление привычек ---
async def delete_habit_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid = update.effective_user.id
    habits = list(user_data.get(uid, {}).get("habits", {}).keys())
    if not habits:
        await update.message.reply_text("У вас нет привычек для удаления.")
        return ConversationHandler.END

    habits_str = "\n".join(f"• {h}" for h in habits)
    await update.message.reply_text(f"Введите название привычки для удаления:\n\n{habits_str}")
    return DELETING_HABIT

async def delete_habit_confirm(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid = update.effective_user.id
    habit = update.message.text.strip()
    if habit in user_data[uid]["habits"]:
        del user_data[uid]["habits"][habit]
        await update.message.reply_text(f"Привычка «{habit}» удалена ❌", reply_markup=main_keyboard)
    else:
        await update.message.reply_text("Такой привычки нет.", reply_markup=main_keyboard)
    return ConversationHandler.END

# --- Просмотр и выполнение привычек ---
async def list_habits(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid = update.effective_user.id
    habits = user_data.get(uid, {}).get("habits", {})
    if not habits:
        await update.message.reply_text("У вас пока нет привычек.")
        return
    text = "📋 Ваши привычки:\n"
    for h, c in habits.items():
        text += f"• {h} — выполнено {c} раз\n"
    text += "\nЧтобы отметить выполнение, просто напишите название привычки."
    await update.message.reply_text(text)

async def complete_habit(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid = update.effective_user.id
    text = update.message.text.strip()
    habits = user_data.get(uid, {}).get("habits", {})
    if text in habits:
        habits[text] += 1
        user_data[uid]["points"] += 10
        user_data[uid]["completed"] += 1
        level = user_data[uid]["level"]
        msg = f"Отлично! Вы выполнили «{text}» 💪 (+10 очков)"

        if user_data[uid]["points"] >= level * 100:
            user_data[uid]["level"] += 1
            msg += f"\n🎉 Уровень повышен до {user_data[uid]['level']}!"

        achievements = check_achievements(uid)
        if achievements:
            msg += "\n\n" + "\n".join(achievements)

        await update.message.reply_text(msg)
    else:
        await update.message.reply_text("Такой привычки нет. Добавьте её через кнопку ✚.")

# --- Статистика ---
async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid = update.effective_user.id
    u = user_data.get(uid)
    if not u:
        await update.message.reply_text("Нет данных.")
        return
    await update.message.reply_text(
        f"📊 Ваша статистика:\n"
        f"Уровень: {u['level']}\n"
        f"Очки: {u['points']}\n"
        f"Всего выполнено привычек: {u['completed']}"
    )

# --- Челленджи ---
async def challenges(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🏆 Текущие челленджи:\n"
        "• 7 дней подряд выполнять привычки — +200 очков\n"
        "• Выполнить 50 привычек — достижение «Железная воля» 💎"
    )

# --- Достижения ---
async def achievements(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid = update.effective_user.id
    a = user_data.get(uid, {}).get("achievements", [])
    if not a:
        await update.message.reply_text("Вы пока не получили ни одного достижения 😔")
        return
    text = "🥇 Ваши достижения:\n" + "\n".join(f"• {x}" for x in a)
    await update.message.reply_text(text)

# --- Рейтинг ---
async def leaderboard(update: Update, context: ContextTypes.DEFAULT_TYPE):
    leaderboard = sorted(
        [(u, d["points"]) for u, d in user_data.items()],
        key=lambda x: x[1],
        reverse=True
    )
    text = "🌍 Рейтинг игроков:\n"
    for i, (uid, pts) in enumerate(leaderboard[:10], start=1):
        text += f"{i}. ID {uid} — {pts} очков\n"
    await update.message.reply_text(text)

# --- Обработка кнопок ---
async def handle_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "📋 Мои привычки":
        await list_habits(update, context)
    elif text == "✚ Добавить привычку":
        return await add_habit_start(update, context)
    elif text == "❌ Удалить привычку":
        return await delete_habit_start(update, context)
    elif text == "📊 Статистика":
        await stats(update, context)
    elif text == "🏆 Челленджи":
        await challenges(update, context)
    elif text == "🥇 Достижения":
        await achievements(update, context)
    elif text == "🌍 Рейтинг":
        await leaderboard(update, context)
    elif text == "ℹ️ Помощь":
        await help_command(update, context)
    else:
        await complete_habit(update, context)

# --- Основная функция ---
def main():
    app = Application.builder().token(BOT_TOKEN).build()

    add_conv = ConversationHandler(
        entry_points=[MessageHandler(filters.Regex("^✚ Добавить привычку$"), add_habit_start)],
        states={ADDING_HABIT: [MessageHandler(filters.TEXT & ~filters.COMMAND, add_habit_save)]},
        fallbacks=[],
    )

    delete_conv = ConversationHandler(
        entry_points=[MessageHandler(filters.Regex("^❌ Удалить привычку$"), delete_habit_start)],
        states={DELETING_HABIT: [MessageHandler(filters.TEXT & ~filters.COMMAND, delete_habit_confirm)]},
        fallbacks=[],
    )

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(add_conv)
    app.add_handler(delete_conv)
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_buttons))

    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
