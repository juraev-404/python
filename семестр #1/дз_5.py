# # 9

from random import randint
# l = input().split(' ')
# M, N = int(l[0]), int(l[1])
# m = [[randint(0, 100) for i in range(N)] for el in range(M)]
# s = 0
# for i in m:
#     s += sum(i)
# for s2 in m:
#     for st1 in range(len(s2)):
#         print('%3.0f' % s2[st1], end=' ')
#     print(' ')
# arf = s/(M*N)
# ch = 0
# ras = []
# for it in range(N):
#     ras.append(0)
#     for el in m:
#         if el[ch] > arf:
#             ras[ch] += 1
#     ch += 1
# print(arf, ras, sep='\n')

# # 15

# l2 = input().split(' ')
# M2, N2 = int(l2[0]), int(l2[1])
# m2 = [[randint(-25, 100) for i in range(N2)] for el in range(M2)]
# ras2 = 0
# ind = -1
# for s3 in m2:
#     for st2 in range(len(s3)):
#         print('%3.0f' % s3[st2], end=' ')
#     print(' ')
# print(' ')
# for it2 in range(M2):
#     for i2 in m2:
#         if i2[ind] < 0:
#             ras2 -= 1
#     if ras2 == 0:
#         for i3 in m2:
#             i3[ind], i3[-N2] = i3[-N2], i3[ind]
#         break
#     ind -= 1
#     ras2 = 0
# for s3 in m2:
#     for st2 in range(len(s3)):
#         print('%3.0f' % s3[st2], end=' ')
#     print(' ')



# l = input().split(' ')
# M, N = int(l[0]), int(l[1])
# m = [[randint(-20, 100) for i in range(N)] for el in range(M)]
# s = 0
# for i in m:
#     s += sum(i)
# for s2 in m:
#     for st1 in range(len(s2)):
#         print('%3.0f' % s2[st1], end=' ')
#     print(' ')
# ch = 0
# ras = []
# for it in range(N):
#     ras.append(0)
#     for el in m:
#         if el[ch] < 0:
#             ras[ch] += 1
#     ch += 1
# print(ras.index(max(ras)))

l = input().split(' ')
M, N = int(l[0]), int(l[1])
m = [[randint(-20, 100) for i in range(N)] for el in range(M)]
s = 0
for i in m:
    s += sum(i)
for s2 in m:
    for st1 in range(len(s2)):
        print('%3.0f' % s2[st1], end=' ')
    print(' ')
ch = 0
for it in range(N):
    for el in m:
        if el[ch] < 0:
            el[ch] == -1*el[ch]
    ch += 1
for s2 in m:
    for st1 in range(len(s2)):
        print('%3.0f' % s2[st1], end=' ')
    print(' ')