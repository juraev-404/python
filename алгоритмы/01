import pandas as pd
arr = pd.read_csv('C:\\Users\\khaiy\\Desktop\\проект\\python\\алгоритмы\\ТА Фин 2026 - ТРПО24-4.csv')
li = [i for i in arr['ФИО'].to_list() if not pd.isna(i)][:-1]
li_n = [i.split()[1] for i in li]
l = []
for i in range(len(li)):
    l.append([li[i], li_n.count(li_n[i])])
print(l)
