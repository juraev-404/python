# Вариант 5 
# а) Реализовать функцию-генератор, которая создает все возможные перестановки элементов 
# списка. 
# б) Реализовать функцию-генератор, которая создает все возможные варианты расположения 
# продуктов на полке в магазине. 
# в) Отфильтровать список чисел, оставив только положительные значения, используя выражение
# генератор. 
# г) Создать список всех троек чисел (a,b,c), где a+b+c=0, используя выражение-генератор: 

# a 
def permutations(lst): return list([x] + p for i, x in enumerate(lst) for p in permutations(lst[:i] + lst[i+1:])) if len(lst) > 1 else [lst]
print(permutations([2,3,5]))
# б 
def shelf_arrangements(products): return permutations(products)
print(shelf_arrangements(['sad', 'day', 'asd']))
# в 
def positive_numbers(numbers): return [x for x in numbers if x > 0]
print(positive_numbers([5, -3, 0, 8, -1, 7]))
# г 
triplets = [(a, b, c) for a in range(-10, 11) for b in range(-10, 11) for c in range(-10, 11) if a + b + c == 0]
print(triplets[:10])