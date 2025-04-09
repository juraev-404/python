class ТРАНСПОРТ():
    def __init__(self, name, mark, number, speed):
        self.name = name
        self.mark = mark
        self.number = number 
        self.speed = speed

    def info(self):
        print(f'названые: {self.name}')
        print(f'марка: {self.mark}')
        print(f'номер: {self.number}')
        print(f'скорость: {self.speed}')

class АВТОМОБИЛЬ(ТРАНСПОРТ):
    def __init__(self, name, mark, number, speed, lcapacity):
        super().__init__(name, mark, number, speed)
        self.lcapacity = lcapacity

    def info(self):
        ТРАНСПОРТ.info(self)
        print(f'грузоподьёмност: {self.lcapacity}т')

class МОТОЦИКЛ(ТРАНСПОРТ):
    def __init__(self, name, mark, number, speed, lcapacity, availability):
        super().__init__(name, mark, number, speed)
        self.lcapacity = lcapacity
        self.availability = availability

    def info(self):
        super().info()
        if self.availability == 'no':
            print(f'грузоподьёмност: 0')
            print(f'наличие каляски: нет')
        else:
            print(f'грузоподьёмност: {self.lcapacity}т')
            print(f'наличие каляски: есть')

class ГРУЗОВИК(ТРАНСПОРТ):
    def __init__(self, name, mark, number, speed, lcapacity, availability):
        super().__init__(name, mark, number, speed)
        self.lcapacity = lcapacity
        self.availability = availability

    def info(self):
        super().info()
        if self.availability == 'no':
            print(f'грузоподьёмност: {self.lcapacity}т')
            print(f'наличие каляски: нет')
        else:
            print(f'грузоподьёмност: {self.lcapacity * 2}т')
            print(f'наличие каляски: есть')
            
    

car1 = ГРУЗОВИК('car1', 14, 666, 120, 100, 'yes')
car2 = АВТОМОБИЛЬ('car2', 50, 777, 200, 10)
car3 = МОТОЦИКЛ('car3', 5, 444, 275, 5, 'yes')
car4 = ГРУЗОВИК('car4', 20, 333, 135, 50, 'yes')

car1.info()

li = [car1, car2, car3, car4]

for i in li:
    if i.lcapacity > 25:
        print(i.name)
