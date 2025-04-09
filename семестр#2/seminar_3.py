# 156

class Student:
    n = 0

    def __init__(self, name):
        self.name = name
        Student.n += 1

    def message(self):
        print("Здравствуйте, я – студент", self.name)

    @staticmethod  # Декоратор
    def kol():
        print('У нас {:d} студента.'.format(Student.n))


st1 = Student('Сергей')
st2 = Student('Макс')
st3 = Student('Ростислав')

st1.message()
st2.message()
st3.message()
Student.kol()

# 159

class Student:
    def __init__(self, name, city, vozr):
        self.name = name
        self.city = city
        self.__vozr = vozr

    @property
    def vozr(self):
        return self.__vozr

    def message(self):
        print("Здравствуйте, я – студент", self.name, "из", self.city, self.vozr)


st1 = Student('Сергей', 'Москвы', '17')
st1.message()