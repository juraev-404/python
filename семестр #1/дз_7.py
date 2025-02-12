from random import randint

#29

l = input().split(' ')
M, N = int(l[0]), int(l[1])
m = [[randint(-100, 50) for i in range(N)] for el in range(M)]
ch = -1
mi = 0
for s2 in m:
    for st1 in range(len(s2)):
        print('%3.0f' % s2[st1], end=' ')
    print(' ')
for i in range(N):
    for el in m:
        if el[ch] < 0:
            mi += 1
        else:
            break
    if mi == M:
        print(N+ch)
        break
    mi = 0
    ch += -1

#30

l2 = input().split(' ')
M2, N2 = int(l2[0]), int(l2[1])
m2 = [[randint(-100, 50) for i in range(N2)] for el in range(M2)]
ch2 = 0
for s in m2:
    for st in range(len(s)):
        print('%3.0f' % s[st], end=' ')
    print(' ')
li = []
for i in range(N2):
    li.append(0)
    for el in m2:
        if el[ch2] < 0:
            li[ch2] += 1
    ch2 += 1
print()
for i2 in range(N2):
    m2[i2][li.index(min(li))], m2[i2][li.index(max(li))] = m2[i2][li.index(max(li))], m2[i2][li.index(min(li))]
for s in m2:
    for st in range(len(s)):
        print('%3.0f' % s[st], end=' ')
    print(' ')