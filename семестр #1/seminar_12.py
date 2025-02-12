with open('file.txt', 'w') as file:
    line_1 = 'В этом примере мы открываем файл "data.pkl" в режиме чтения байтов ("rb"). Затем мы используем функцию pickle.load(), чтобы загрузить данные из файла в переменнуюloaded_data и выводим ее значение на экран.'
    line_2 = 'Модуль pickle также предоставляет другие функции, такие как pickle.dumps() (сериализация в строку), pickle.loads() (десериализация из строки), pickle.dump() и pickle.load() для работы с сокетами. Важно отметить, что модуль pickle может использоваться только в среде, где нет доверия небезопасным данных.'
    line_3 = 'При десериализации объектов из ненадежных источников может быть выполнен вредоносный код. Поэтому, будьте осторожны при использовании pickle с данными, полученными из ненадежных источников.'
    file.writelines([line_1, line_2, line_3])


#5

k = int(input())
with open('file.txt', 'r') as file_r:
    lines = file_r.readlines()
    nl = 1
with open('file.txt', 'w') as file_W:
    for line in lines:
        if nl != k:
            file_W.write(line)
        nl += 1

with open('file.txt', 'r') as file_r:
    print(file_r.read())

#5

with open('date.txt', 'w') as date:
    date.write('20.11.2008, 30.04.1999, 10.12.1998')


with open('date.txt', 'r') as date:
    dt = date.read()
    dt = dt.split(', ')
    li = []
    for i in dt:
        li.append(i.split('.'))
with open('date.txt', 'w') as date:
    li2 = []
    for i in li:
        li2.append(i[2])
    m = li2.index(min(li2))
    print('.'.join(li[m]))
