from random import randint
S = 'a s f s e d'
N = randint(1, 10)
l = S.split(' ')
l2 = []
for i in l:
    l2.append(i+'*'*N)
print(''.join(l2))

ned = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
l3 = input().split(' ')
M, N = int(l3[0]), int(l3[1])
m = [[ned[randint(0, 6)] for i in range(N)] for el in range(M)]
print(m)

for i in m:
    print(i)