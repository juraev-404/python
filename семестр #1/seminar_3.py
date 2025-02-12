a = input()
b = 0
for i in range(int(a)):
    if i == 0:
        continue
    if int(a) % i == 0:
        b += i
    else:
        pass
if int(a) == b:
    print('число '+ a + ' совенршенно')

# 29

N = input()
N = N.split(" ")
l = []
for i in N:
    j = 0
    j_c = 0
    for el in i:
        j += int(el)
        j_c += 1 
    n = 'среднее арифметическое числа '+i+': '+str(j/j_c)
    l.append(n)
print(l)

# 30

N2 = input()
N2 = N2.split(' ')
l2 = 0
for i in N2:
    for el in i:
        if int(el) % 2 == 0:
            l2 += 1
        else:
            pass
print(l2)

# 1

n1 = int(input())
s = 0
for i in range(n1+1):
    if i == 0 :
        continue
    s += 1/2**i
print(s)

import math

# 2

n2 = int(input())
x = int(input())
s2 = 0
for i in range(1, n2+1):
    s2 += math.cos(x)**n2/n2
print(s2)

# 3

n3 = int(input())
s3 = 0
for i in range(1, n3+1):
    s3 += 1 + (-1)**n3*3**n3
print(s3)

#  4 

n4 = int(input())
s4 = 0
for i in range(1, n4+1):
    s4 += 1/math.sin(i)
print(s4)

# 5

n5 = int(input())
s5 = 0
for i in range(1, n5+1):
    s5 += 1 + (-1)**(n5+1)*n5**3
print(s5)