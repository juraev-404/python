# a = 'семинар игра сериал лекция'
# c = len(a.split(' '))
# print(c)

# # 2

# l = 'Семинар Игра Сериал Транспорт'
# l1 = l.lower().split()
# con = 0
# for i in l1:
#     if i[0] == i[-1]:
#         con += 1
#     else:
#         pass
# print(con)

# # 3

# li = 'Семинар Игра Сериал Транспорт Академия'
# l2 = li.split()
# c1 = 0
# for i2 in l2:
#     for i3 in range(len(i2)):
#         if i2[i3] == 'А':
#             c1 += 1
#         else:
#             pass
# print(c1) 

# # 4

# l4 = 'Семинар Игра Сериал Транспорт Академия'
# l4_1 = l4.split()
# l4_2 = []
# for i in l4_1:
#     l4_2.append(len(i))
# print(min(l4_2))

# # 5
# l5 = 'Семинар Игра Сериал Транспорт Академия'
# l5_2 = l5.split()
# l5_1 = list(reversed(l5_2))
# l5_3 = ' '.join(l5_1)
# print(l5_3)

# # 6

# l6 = 'СЕГОДНЯ ХОРОШИЙ ДЕНЬ'


# # задача 1.4

# # 3

# stroka = 'Сегодгя Серёжа пошел в школу лСало'
# new = ''
# a = stroka.split()
# bukva = stroka[0]
# x = 0
# for i in a:
#     if i[0] == bukva and x != 0:
#         new = new + '$' + i[1:] + ' '
#     else:
#         new = new + i + ' '
#     x = 1
# print(new)

# # 4 

# s4 = 'Сегодгя Серёжа пошел в школу лСало'
# s5 = 'ХОРОШИЙ ДЕНЬ'
# a = s4[:2]
# b = s5[:2]
# print(b + s4[2:] + ' ' + a + s5[2:])

# # 5

# sl = 'classing'
# if len(sl) >= 3:
#     if sl[-3:] == 'ing':
#         print(sl[0:-3]+'ly')
#     elif sl[-3:-1] != 'ing':
#         print(sl+'ing')
#     else:
#         print(sl)

# # 6

# a6 = 'ХОРОШИЙ ДЕНЬ' 
# n = int(input())
# for i in range(0, len(a6)):
#     if (i+1)%n==0:
#         pass
#     else:
#         print(a6[i], end='')

# # 7

# s7 = 'ХОРОШИЙ ДЕНЬ' 
# print(s7[-1]+ s7[1:-1] + s7[0])

# # 8

# st = 'class'
# li1 = list(st)
# for i in range(len(li1)):
#     if i%2 == 1:
#         li1.pop(i)
# print("".join(li1))

# 7

st7 = 'Сегодгя *Серёжа* пошел*  *в школу'

if st7.find('*') == -1:
    print('звезд нет')
else:
    print(st7.find('*'), 'индекс 1 звезди', sep=': ')
    a = st7.find('*')
    st7_2 = st7.replace(st7[a], '', 1)
    if st7_2.find('*') == -1:
        pass
    else:
        if st7_2.find('*') == st7_2.rfind('*'):
            print(st7_2.find('*')+1, 'индекс последной звезди', sep=': ')
        else:
            print(st7_2.find('*')+1, 'индекс 2 звезди', sep=': ')
            print(st7_2.rfind('*')+1, 'индекс последной звезди', sep=': ')
            st7_2[st7_2.rfind('*'):].replace('*', '', 1)
            print(st7_2[:st7_2.rfind('*')]+st7_2[st7_2.rfind('*'):].replace('*', '', 1))



