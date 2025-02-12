from random import randint
import csv

# 3

ned = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
l = input().split(' ')
M, N = int(l[0]), int(l[1])
m = [[ned[randint(0, 6)] for i in range(N)] for el in range(M)]
print(m)

for i in m:
    print(i)

with open('matrix.csv', 'w') as file:
    file_csv = csv.writer(file, delimiter=';', lineterminator='\r')
    file_csv.writerows(m)

# 4

import csv
with open('C:\\Users\\khaiy\\Desktop\\проект\\python\\Книга(Лист1).csv', 'r') as f:
    a = csv.reader(f)
    header = next(a)
    data = list(a)
    for i in range(len(data)):
        data[i] = data[i][0].split(';')
    sr = 0
    count = 0
    for i in data:
        sr += float(i[1])
        count += 1
    sr = sr/count
    for i in range(len(data)):
        if float(data[i][1]) > sr:
            r = float(data[i][1]) - sr
            data[i][1] = sr
            data[i].append(r)
        else:
            data[i].append('None')
    data.insert(0, ['name', 'price', 'r'])

with open('Книга(Лист1).csv', 'w') as file:
    file_csv = csv.writer(file, delimiter=';', lineterminator='\r')
    file_csv.writerows(data)

# 5 

def func(mn, wn, t):
    for i in t:
        if i[2] == 'м':
            with open(f'{mn}.csv', 'a') as file:
                file_csv = csv.writer(file, delimiter=';', lineterminator='\r')
                file_csv.writerow(i)

        else:
            with open(f'{wn}.csv', 'a') as file:
                file_csv = csv.writer(file, delimiter=';', lineterminator='\r')
                file_csv.writerow(i)

li = [('Сергей', 22, 'м'), ('Светлана', 32, 'ж'), ('Ирина', 27, 'ж'), ('Евгений', 45, 'м')]
func('man', 'woman', li)

    