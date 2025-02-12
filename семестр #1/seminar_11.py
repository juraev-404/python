def func(n):
    if n==1 or n==0:
        return 1
    else:
        return n*func(n-2)
print(func(8))

# p = 0
# a = 0
# def func(n):
#     global p, a
#     p += n[a]
#     a += 1
#     if a == len(n):
#         return p
#     return func(n)
# c = [1, 2, 3, 8]
# print(func(c))

# def func(n, x):
#     if n > 0:
#         return x * func(n - 1, x)
#     elif n == 0:
#         return 1
#     else:
#         n *= -1
#         return 1/(x * func(n - 1, x))
# print(func(-3, 10))

# p = 0
# a = 0
# def func(n):
#     global p, a
#     p = n[a]
#     a += 1
#     if p > n[a+1]:
#         p = n
#     else:
#         pass
#     if a == len(n)-2:
#         return p
#     else:
#         return func(n)
# c = [1, 2, 3, 8]
# print(func(c))

# ras = lambda x, y: x*y 
# print(ras(5, 3))

# ras = lambda x: 'да' if len(x)==4 else 'нет'
# a = [3,5,6,34]
# ras = list(filter(lambda x: x if x%2==0 else None, a))
# print(ras)

# ras = list(map(lambda x: x if x%2==0 else a.pop(), a))
# print(ras)

