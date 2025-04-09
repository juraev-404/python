# 2
class Summa():
    def __init__(self, n1,n2):
        self.a = n1
        self.b = n2
        
    def sum(self):
        s = self.a + self.b 
        print(s)

s = Summa(int(input()), int(input()))
s.sum()


# 157

class Stuend():
    def __init__(self, name, city, vozr):
        self.name = name
        self.city = city
        self.__vozr = vozr

    def message(self):
        print(f'Здравствуйте я студент {self.name}, из {self.city} {self.__vozr}')

st = Stuend('Сергей', 'Моквы', '18')        
st.message()

# 158

class Student:
    def __init__(self, name, city, vozr):
        self.name = name
        self.city = city
        self.__vozr = vozr

        self.__talk()

    def __talk(self):
        print("Начим урок")

    def message(self):
        print("Здравствуйте, я – студент", self.name, "из", self.city, self.__vozr)

st1 = Student('Сергей', 'Москва', '17')
st1.message()

# 161

class Human():
    name = ""

    def __init__(self):
        print("Создан класс Человек")

# ----

class Prepod(Human):
    kafedra = ""
    dolgnost = ""

# ----

class Student(Human):
    fakultet = ""
    gruppa = ""

# ----

h = Human()
pr = Prepod()
st = Student()

# 162

class Human():
    name = ""

    def __init__(self):
        print("Создан класс Человек")

# ----

class Prepod(Human):
    kafedra = ""
    dolgnost = ""

    def __init__(self):
        print("Создан класс Преподаватель")

# ----

class Student(Human):
    fakultet = ""
    gruppa = ""

    def __init__(self):
        print("Создан класс Студент")

# ------ Создание экземпляров классов -------
h = Human()
pr = Prepod()
st = Student()

# 163

class Human():
    name = ""

    def __init__(self):
        print("Создан класс Человек")

# ----

class Prepod(Human):
    kafedra = ""
    dolgnost = ""

    def __init__(self):
        Human.__init__(self)
        print("Создан класс Преподаватель")

# ----

class Student(Human):
    fakultet = ""
    gruppa = ""

    def __init__(self):
        Human.__init__(self)
        print("Создан класс Студент")

# ------ Создание экземпляров классов -------
h = Human()
pr = Prepod()
st = Student()

# 164

class Human():
    def __init__(self, name):
        self.name = name
        print("Создан класс Человек")

    def info(self):
        print(self.name, end=" ")

# ----

class Prepod(Human):
    def __init__(self, name, kafedra, dolgnost):
        Human.__init__(self, name)
        self.kafedra = kafedra
        self.dolgnost = dolgnost
        print("Создан класс Преподаватель:", self.name)

    def info(self):
        Human.info(self)
        print("Кафедра: {} Должность: {}".format(self.kafedra, self.dolgnost))

# ----

class Student(Human):
    def __init__(self, name, fakultet, gruppa):
        Human.__init__(self, name)
        self.fakultet = fakultet
        self.gruppa = gruppa
        print("Создан класс Студент:", self.name)

    def info(self):
        Human.info(self)
        print("Факультет: {} Группа: {}".format(self.fakultet, self.gruppa))

# ----

pr = Prepod("Сергей Гуриков", "Информатика", "Доцент")
pr.info()
print()

st = Student("Макс Рыжиков", "ОТФ-1", "ТРПО24-5")
st.info()