# c = 0
# for i in range(10, 100):
#     if i % 3 == 0:
#         c += 1
# print(c)

# #2

# l = [-1, 2, 35, -4, 5, 67, -7, 8, 9]
# # k = input(f'1<k<l<{len(l)} k: ')
# # L = input(f'1<k<l<{len(l)} l: ')
# # a = 0
# # b = 0
# # for i in l:
# #     if l.index(i)<int(k) or l.index(i)>int(L):
# #         a += int(i)
# #         b += 1
# # print(a/b)

# #5

# # l1 = []
# # l2 = []
# # for el in l:
# #     if el % 2 == 0:
# #         l1.append(el)
# #     else:
# #         l2.append(el)
# # print(l1, l2, sep='\n')

# # print(list(reversed(sorted(l2))))
# # print(list(sorted(l1)))


# # #3

# # l = [-1, 2, 35, -4, 5, 67, -7, 8, 9]
# # l3 = []
# # for i2 in l:
# #     if i2 > 0:
# #         l3.append(i2)
# # print(list(reversed(sorted(l3))))

# # #17

# # l = [-1, 2, 35, -4, 5, 67, -7, 8, 9]
# # l7 = []
# # for i in l:
# #     if i>9 and i<100:
# #         l7.append(str(i).split())
# # for i in range(len(l7-1)):
# #     for j in range(len(l7-1-i)):
# #         if l7[j][1] > l7[j+1][1]:
# #             l7[j][1], l7[j+1][1] = l7[j][1+1], l7[j][1]
    

# #20

# # li = [23, 44, 62, 86, 55, 79]
# # li2 = []
# # k = int(input())
# # for i in li:
# #     li2.append(i % k)
# # li2 = sorted(li2)
# # for i in li:
# #     e = i % k
# #     print(li2.index(e))

# # 18
# l9 = [123, 786, 456, 321, 435,795]
# l8 = []
# for i8 in l9:
#     b8 = 0
#     for i9 in str(i8):
#         b8 += int(i9)
#     l8.append([i8, b8])
# print(l8)
# for i in range(len(l8)-1):
#     for j in range(len(l8)-1-i):
#         if l8[j][1] < l8[j+1][1]:
#             l8[j], l8[j+1] = l8[j+1], l8[j]
# print(l8)


# li = [23, 44, 62, 86, 55, 79]
# li2 = []
# k = int(input())
# for i in li:
#     li2.append([i, i % k])
# for i20 in range(len(li2)-1):
#     for u in range(len(li2)-1-i20):
#         if li2[u][1] < li2[u+1][1]:
#             li2[u], li2[u+1] = li2[u+1], li2[u]
# print(li2)

# l = [[2, 5], [6, 8], [9, 1]]
# for el in range(l[0]):
#     for i in l:
#         if i[el]

a = [[0, 2, 3, 7], [7, 6, 9, 4], [7, 9, 1, 1], [7, 3 , 5, 7]]
for i in range(len(a)):
    b = []
    c = 0
    for i2 in a:
        b.append(i2[i])
    for i3 in b:
        if i3 % 2 != 0:
            c += 1
    if c == 4:
        print(i)            
    



