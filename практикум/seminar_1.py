import tkinter as tk
import math

# --- функции ---

def draw_tree(x, y, angle, length, depth):
    """Рекурсивная отрисовка ветвей"""
    if depth == 0:
        return

    # конечная точка ветви
    end_x = x - length * math.sin(math.radians(angle))
    end_y = y - length * math.cos(math.radians(angle))

    # рисуем линию
    canvas.create_line(x, y, end_x, end_y, width=depth/2, fill='white')

    # рекурсивные вызовы для левой и правой ветви
    new_length = length * 0.7   # фиксированное уменьшение длины
    draw_tree(end_x, end_y, angle - angle_var.get(), new_length, depth - 1)
    draw_tree(end_x, end_y, angle + angle_var.get(), new_length, depth - 1)


def update_tree(event=None):
    """Перерисовка дерева"""
    canvas.delete("all")
    draw_tree(start_x, start_y, 0, start_length, max_depth)
    info_text = f"Угол: {angle_var.get():.1f}°"
    canvas.create_text(400, 550, text=info_text, font=("Arial", 12), fill='white')


# --- окно и интерфейс ---

root = tk.Tk()
root.title("Фрактальное дерево")

# холст
canvas = tk.Canvas(root, width=800, height=600, bg='black')
canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# панель управления
control_frame = tk.Frame(root)
control_frame.pack(side=tk.BOTTOM, fill=tk.X)

# угол
tk.Label(control_frame, text="Угол ветвления:").pack(side=tk.LEFT)
angle_var = tk.DoubleVar(value=0)
angle_slider = tk.Scale(control_frame, from_=0, to=360,
                        orient=tk.HORIZONTAL, variable=angle_var,
                        command=update_tree, length=400)
angle_slider.pack(side=tk.LEFT, fill=tk.X, expand=True)

# --- параметры дерева ---
start_x = 400
start_y = 500
start_length = 120
max_depth = 10

# первый вызов
update_tree()

# запуск цикла
root.mainloop()
