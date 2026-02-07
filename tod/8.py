import re

# Загрузим данные
with open('movies.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

first_words = []
last_words = []
middle_words = []

for line in lines:
    parts = line.strip().split('\t')
    if len(parts) < 2:
        continue
    title = parts[1]

    # Удалим год и знаки препинания кроме &
    title = re.sub(r'\s*\(\d{4}\)', '', title)
    words = re.findall(r'\b\w+&?\w*\b', title)

    if not words:
        continue

    # Группировка слов
    first_words.append(words[0])
    if len(words) > 1 and words[-1] != words[0]:
        last_words.append(words[-1])
    if len(words) >= 3:
        middle_words.extend(words[1:-1])

# Функция для выбора двух самых длинных уникальных слов
def get_top2_longest(words):
    unique_words = list(set(words))
    unique_words.sort(key=lambda w: (-len(w), w))
    return unique_words[:2]

# Получаем результат
first = get_top2_longest(first_words)
last = get_top2_longest(last_words)
middle = get_top2_longest(middle_words)

# Финальный список
final_list = first + last + middle

# Вывод
print(final_list)
