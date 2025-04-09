class Persona():
    vozr = 0
    def __init__(self, name, date, tdate):
        self.name = name
        self.date = date
        self.tdate = tdate
    def vozrast(self):
        self.vozr = self.tdate - self.date
    def info(self):
        print("\nСоздан класс Персона")
        print("Фамилия Имя: {0} Возраст: {1}".format(self.name, self.vozr))

# Создание дочерних классов

class Abiturient(Persona):
    def __init__(self, name, date, tdate, fakultet):
        super().__init__(name, date, tdate)
        self.fakultet = fakultet
    def info(self):
        Persona.vozrast(self)
        Persona.info(self)
        print("Создан класс Абитуриент")
        print("Факультет: {0}".format(self.fakultet))

class Student(Persona):
    def __init__(self, name, date, tdate, fakultet, kurs):
        super().__init__(name, date, tdate)
        self.fakultet = fakultet
        self.kurs = kurs
    def info(self):
        Persona.vozrast(self)
        Persona.info(self)
        print("Создан класс Студент")
        print("Факультет: {0} Курс: {1}".format(self.fakultet, self.kurs))

class Prepodavatel(Persona):
    def __init__(self, name, date, tdate, fakultet, dolgnost, staj):
        super().__init__(name, date, tdate)
        self.fakultet = fakultet
        self.dolgnost = dolgnost
        self.staj = staj
    def info(self):
        Persona.vozrast(self)
        Persona.info(self)
        print("Создан класс Преподаватель")
        print("Факультет: {0} Должность: {1} Стаж: {2}".format(self.fakultet, self.dolgnost, self.staj))

# Основная часть программы

itogspisok = []
n = int(input("Введите количество персон: "))
tdate1 = int(input("Введите текущий год: "))

for i in range(n):
    persona = input("Кто вы? 1) Абитуриент, 2) Студент, 3) Преподаватель ")
    name1 = input("Введите вашу фамилию и имя: ")
    date1 = int(input("Введите год рождения: "))
    spisok = [name1, date1]
    itogspisok.append(spisok)

    if persona == "1":
        fakultet1 = input("Введите факультет: ")
        abitur = Abiturient(name1, date1, tdate1, fakultet1)
        abitur.info()
        print()

    if persona == "2":
        fakultet1 = input("Введите факультет: ")
        kurs1 = input("Введите курс: ")
        stud = Student(name1, date1, tdate1, fakultet1, kurs1)
        stud.info()
        print()

    if persona == "3":
        fakultet1 = input("Введите факультет: ")
        dolgnost1 = input("Введите должность: ")
        staj1 = input("Введите стаж работы: ")
        prepod = Prepodavatel(name1, date1, tdate1, fakultet1, dolgnost1, staj1)
        prepod.info()
        print()

print("Далее будут отобраны персоны, чей год рождения попадает в заданный промежуток")
diapazon1 = int(input("Введите начало промежутка: "))
diapazon2 = int(input("Введите конец промежутка: "))
print("\nПерсоны, удовлетворяющие заданному условию:")
for i in range(len(itogspisok)):
    if (itogspisok[i][1] >= diapazon1) and (itogspisok[i][1] <= diapazon2):
        print("Фамилия Имя:", itogspisok[i][0], "Год рождения:", itogspisok[i][1])