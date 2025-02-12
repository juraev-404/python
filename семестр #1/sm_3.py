# 5 
import csv

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