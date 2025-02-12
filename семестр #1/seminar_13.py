# a = input('введите имя файла')

# with open(a, 'r') as f:
#     q = f.readlines()
#     print(q)

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

