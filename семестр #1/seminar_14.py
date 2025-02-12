import paket.min_max
li = [5, 3, 4, 8, 6]
print(paket.min_max.minimum(li))
print(paket.min_max.maximum(li))

import csv

li = [('Сергей', 22, 'м'), ('Светлана', 32, 'ж'), ('Ирина', 27, 'ж'), ('Евгений', 45, 'м')]

with open('file.csv', 'w') as file:
    file_csv = csv.writer(file, delimiter=';', lineterminator='\r')
    file_csv.writerows(li)

li = [5, 9, 2, 3, 64, 94, 55, 68]

def nt(l, nd=0):
    if nd+1 == len(li):
        return 1
    else:
        if li[nd]%2==1:
            with open('file_2.txt', 'a') as file:
                file.write(str(li[nd])+', ')
                return nt(l, nd+1)
        else:
            return nt(l, nd+1)
nt(li)


import matplotlib.pyplot as plt
import math


# x = [3,5,7,-8]
# y = [6,3,7,-2]
# x1 = [i for i in range(-5, 5)]
# y1 = [i**2 for i in x1]
# plt.plot(x,y)
# plt.plot(x1, y1)
# plt.grid()
# plt.xlabel('Ось x')
# plt.ylabel('Ось y')
# plt.title('График')
# plt.legend(('f1', 'f2'))
# plt.show()

# x = [3,5,7,8]
# y = [i + math.e**(math.sin(i)) for i in x]
# x1 = [2, 6, 9, 4]
# y1 = [5 + math.sin(6*i+4)+8 for i in x1]
# plt.plot(x,y)
# plt.plot(x1,y1)
# plt.xlabel('Ось x')
# plt.ylabel('Ось y')
# plt.title('График')
# # plt.show()
# print(math.e)


x = [i for i in range(4,9)]
y = [(i**2 - 18*i + 77.5)/(i-9) for i in x]
plt.plot(x,y, 'b--.')
plt.xlabel('Ось x')
plt.ylabel('Ось y')
plt.title('График')
plt.grid()
plt.show()