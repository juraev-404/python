# a = input('строка №1: ')
# b = input('строка №2: ')
# c = input('строка №3: ')
# print(set(a + b))
# for i in set(c):
#     s = 'из символов первых двух строк нельзя получить третью строку'
#     if i in set(a + b):
#         pass
#     else:
#         break
#     s = 'из символов первых двух строк можно получить третью строку'
# print(s)

st = 'ten,one,five,two,three,four'
li = st.split(',')
dc = {}
for i in range(len(li)):
    dc[li[i]] = dc.get(st,i) + 1
print(dc)

# st = 'яблоки груши яблоки киви сливы киви'
# li = st.split(' ')
# dc1 = {}
# for i in li:
#     dc1[i] = dc1.get(i,0) + 1
# print(dc1)
# dc2 = {}
# # dc3 = 
# for k, v in dc3.items():
#     mx = max(dc1.values())
#     if mx == v:
#         dc2[k] = dc2.get(k,mx)
#         dc1.pop(k, None)

# print(dc2)

#5 дз

# a1=['Афонини', 'Иванов', 'Евсеенко']
# a2 = ['Афонини', 'Задунаев', 'Евсеенко', 'Кухта']
# a3 = ['Задунаев', 'Евсеенко', 'Кухта', 'Лапугов']

# a = {'миша': ['английский', 'францезский', 'немецкий'], 'тимур': ['английский', 'латинский', 'испанский'], 'амин': {['английский', 'русский', 'испанский']}}

# №1

a = (5, 4, 6, 9)
print(a[0])
a = tuple(reversed(list(a)))
a = reversed(a)
print(a)

def func(*args):
    print(type(args))
func(5,2)

def Circle(R):
    s = 3.14*(R**2)
    p = 2*3.14*R
    return s, p
print(Circle(5))

def Quarter(x, y):
    if x > 0 and y > 0:
        return 1
    if x > 0 and y < 0:
        return 2
    if x < 0 and y < 0:
        return 3
    if x < 0 and y > 0:
        return 4
# print
a = '54'
print(10**0)