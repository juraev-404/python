# from random import randint
# M, N = input().split()
# M = int(M)
# N = int(N)
# A = [[randint(-20, 100) for i in range(N)] for el in range(M)]
# K1, K2 = input().split()
# def del_st():
#     a = 0
#     for i in A:
#         for el in range(len(i)):
#             if K2 > M and K2 > a and a > K1:
#                 A.pop(a)
#     a += 1
# print(A)

S = input()
def CompressStr():
    sl = []
    l = ['',0]
    for i in S:
        if i == l[0]:
            l[1] += 1
        if l[1] > 3 and i != l[0]:
            sl[-1:l[1]] = l[1]
            l[0] = i
        l.append(i)
        return sl
print(''.join(CompressStr()))