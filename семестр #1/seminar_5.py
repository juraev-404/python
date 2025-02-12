# a = int(input())
# b = 1
# while a != 0 and 1!= a:
#     b *= a
#     a -= 2
# print(b)

# 4


# while True:
#     st = input()
#     if len(st) == 0:
#         print('пустая строка!')
#         continue
#     elif st =='STOP':
#         print('program interruped by user')
#         continue
#     print(f'|{st:_^30}|')
#     break

a = 'Хороший день'
b = 'Сегодгя'
for i in a:
    c = b.find(i)-1
    print(f'{c} символ встречается в строке поиска:')