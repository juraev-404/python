#2 

# st = 'яблоки, груши, яблоки, киви, сливы, киви'
# li = st.split(', ')
# dc = {}
# for i in li:
#     dc[i] = dc.get(i,0) + 1
# print(dc)
# mx = max(dc.values())
# for k, v in dc.items():
#     if v == mx:
#         print(k)

#3

# st = {'два': 2, 'три': 3, 'четыре': 4, 'пять': 5, 'двадцать': 20, 'тридцать': 30, 'сорок': 40, 'пятьдесят': 50}
# a = 'тридцать'
# s = a.split()
# if len(s) == 2:
#     ras = st.get(s[0]) + st.get(s[1]) **0.5
# else:
#     ras = st.get(s[0])**0.5
# print(ras)
 
#4

# li = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
# dc = {}
# a = 1
# st = '1 марта 2021'
# li2 = st.split()
# for i in li:
#     dc[i] = dc.get(i, 0) + a
#     a+=1
# st2 = ''
# for i in li2:
#     if i in dc:
#         if dc[i] < 10:
#             st2 += '.'+ '0' + str(dc[i]) + '.'
#         else:
#             st2 += '.'+str(dc[i]) + '.'
#     else:
#         st2 += i
# print(st2)

#5

# st = input()
# dc = {}
# a = 1
# for i in st:
#     dc[i] = 1
#     a += 1
# print(dc)

#6

# l1 = list('abcd')
# d1 = {'c': 5, 'd': 6, 'e': 7, 'f': 8, 'g': 9, 'h': 10}
# ras = 0
# for i in l1:
#     if i in d1:
#         ras+= 1
# print(ras)

#7

# asb = {'м': '-.', 'п': '.-', 'а': '.-.', 'и': '-.-'}
# st = '-. .-. -. .-.   -.-   .- .-. .- .-.'
# li = st.split('   ')
# li2 = []
# for i in li:
#     li2.append(i.split( ))
# st2 = ''
# for el in li2:
#     for el2 in el:
#         for k, v in asb.items():
#             if v == el2:
#                 st2 += k 
#     st2 += ' '
# print(st2)

# from random import randint
# A = set()
# B = set()
# while len(A)!=10:
#     A.add(randint(1, 20))
# while len(B)!=5:
#     B.add(randint(1, 20))
# a = A|B 
# p = A&B 
# r = A-B
# m = A|B - p
# print(A, B)
# print(a, p, r)
# if A - B == set():
#     print('А подмножество В')
# else:

# st = '365+2-428+13216***62asdasd'
# a = {'+', '-', '*', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
# ras = 0
# for i in st:
#     if i in a:
#         ras+=1
# print(ras)

while True: print(eval(input('>>>')))