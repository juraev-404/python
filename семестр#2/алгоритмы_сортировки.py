# Необходимо отсортировать массив строк по длине и вывести результат на экран. В 
# зависимости от переданного параметра отсортировать массив строк по возрастанию 
# длины или по убыванию длины, используя алгоритмы сортировки: сортировку выбором, 
# сортировку пузырьком и быструю сортировку. Сравнить время выполнения алгоритмов 
# сортировки с помощью декоратора. Строки хранятся в файле. 


import time
from functools import wraps

# Декоратор для замера времени
def timeit(func):
    @wraps(func)
    def wrapper(arr, reverse=False):
        start = time.perf_counter()
        result = func(arr.copy(), reverse=reverse)
        end = time.perf_counter()
        print(f"{func.__name__} took {end - start:.6f} seconds")
        return result
    return wrapper

# Сортировка выбором
@timeit
def selection_sort(arr, reverse=False):
    n = len(arr)
    for i in range(n):
        selected = i
        for j in range(i + 1, n):
            if (len(arr[j]) < len(arr[selected])) ^ reverse:
                selected = j
        arr[i], arr[selected] = arr[selected], arr[i]
        print(arr)
    return arr

# Сортировка пузырьком
@timeit
def bubble_sort(arr, reverse=False):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if (len(arr[j]) > len(arr[j + 1])) ^ reverse:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Быстрая сортировка
@timeit
def quick_sort(arr, reverse=False):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if (len(x) < len(pivot)) ^ reverse]
    right = [x for x in arr[1:] if not (len(x) < len(pivot)) ^ reverse]
    return quick_sort(left, reverse) + [pivot] + quick_sort(right, reverse)

# Чтение строк из файла
def read_lines_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]

# Основная функция
def main():
    filename = "strings.txt"  # путь к файлу
    strings = read_lines_from_file(filename)
    strings = ["яблоко sadasd sad s", "банан asda awd sda", "вишня asdw czlk klm", "груша asda lk sasw", "дыня skdk"]


    print("\n--- Сортировка по возрастанию длины ---")
    print("Выбором:", selection_sort(strings, reverse=False))
    print("Пузырьком:", bubble_sort(strings, reverse=False))
    print("Быстрая:", quick_sort(strings, reverse=False))

    print("\n--- Сортировка по убыванию длины ---")
    print("Выбором:", selection_sort(strings, reverse=True))
    print("Пузырьком:", bubble_sort(strings, reverse=True))
    print("Быстрая:", quick_sort(strings, reverse=True))

if __name__ == "__main__":
    main()

