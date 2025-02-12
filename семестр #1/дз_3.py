# 27

a = int(input())
b = int(input())
c = max(a, b)
while 0 > -1:
    c += max(a, b)
    print(c)
    if c % a == 0 and c % b == 0:
        print(f'НОК {a} и {b}: {c}')
        break
    else:
        pass

while 0 > -1:
    c += max(a, b)
    print(c)
    if c % a == 0 and c % b == 0:
        print(f'НОК {a} и {b}: {c}')
        break
    else:
        pass

#28

a2 = input().split(', ')
b2 = []
c2 = 0
for i in a2:
    b2.append(i.split(' '))
    e = int(b2[c2][0])
    f = int(b2[c2][1])
    d = min(e, f)
    while 1==1:
        if e % d == 0 and f % d == 0:
            print(f'НОД {e} и {f}: {d}')
            break
        d -= 1
    c2 += 1