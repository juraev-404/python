# # import csv

# from paket import length 
# # print(length.dm('1000см'))

# from file import csv_module

# a = csv_module.load_table('main_2', True)
# print(a)

# # csv_module.print_table('main')

# b = csv.writer(a, delimiter=';', lineterminator='\r')
# b.writerow('1234567aadsfdsadvzdcv89')

# # csv_module.save_table('main')

# print(csv_module.get_rows_by_number('main_2', 1, 5, True))

# print(csv_module.get_rows_by_index('main', 'main', 2, 4, copy_table=True))

# print(csv_module.get_column_types('main_2'))

# print(csv_module.set_column_types('main_2', 3, 'str'))

# print(csv_module.get_values('main_2', '5'))

# print(csv_module.get_value('main', 5))

# print(csv_module.set_values('main', [0,1,2,3,4,5,6,7], 5))

# text = 'Eeny, meeny, miney, moe; Catch a tiger by his toe.'

# # Создаем связанный список
# def create_linked_list(string):
#     head = None
#     current = None
#     for char in string:
#         node = [char, None]
#         if head is None:
#             head = node
#         else:
#             current[1] = node
#         current = node
#     return head

# # Удаляем узлы с гласными буквами
# def remove_vowels(head):
#     vowels = set("aeiouAEIOU")
#     while head and head[0] in vowels:
#         head = head[1]
    
#     current = head
#     while current and current[1]:
#         if current[1][0] in vowels:
#             current[1] = current[1][1]
#         else:
#             current = current[1]
#     print(head)
#     return head

# # Преобразуем связанный список обратно в строку
# def linked_list_to_string(head):
#     result = []
#     while head:
#         result.append(head[0])
#         head = head[1]
#     return ''.join(result)

# # Решение задачи
# linked_list = create_linked_list(text)
# linked_list = remove_vowels(linked_list)
# result = linked_list_to_string(linked_list)

# print(result)





# text = 'Eeny, meeny, miney, moe; Catch a tiger by his toe.'

# # Создаем двусвязный список
# def create_doubly_linked_list(string):
#     head = None
#     current = None
#     for char in string:
#         node = [None, char, None]  # [prev_node, data, next_node]
#         if head is None:
#             head = node
#         else:
#             current[2] = node  # Устанавливаем ссылку на следующий узел
#             node[0] = current  # Устанавливаем ссылку на предыдущий узел
#         current = node
#     return head

# # Удаляем узлы с гласными буквами
# def remove_vowels(head):
#     vowels = set("aeiouAEIOU")
#     current = head

#     # Перебираем все узлы
#     while current:
#         if current[1] in vowels:  # Если данные узла - гласная
#             prev_node = current[0]
#             next_node = current[2]

#             # Удаляем текущий узел, обновляя ссылки
#             if prev_node:
#                 prev_node[2] = next_node
#             if next_node:
#                 next_node[0] = prev_node

#             # Если текущий узел - голова списка, обновляем head
#             if current == head:
#                 head = next_node
#         current = current[2]  # Переходим к следующему узлу
#     print(head)
#     return head

# # Преобразуем двусвязный список обратно в строку
# def doubly_linked_list_to_string(head):
#     result = []
#     current = head
#     while current:
#         result.append(current[1])
#         current = current[2]
#     return ''.join(result)

# # Решение задачи
# doubly_linked_list = create_doubly_linked_list(text)
# doubly_linked_list = remove_vowels(doubly_linked_list)
# result = doubly_linked_list_to_string(doubly_linked_list)

# print(result)

print(2//3)