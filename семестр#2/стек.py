class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        """Добавляет элемент в стек"""
        self.items.append(value)

    def pop(self):
        """Удаляет верхний элемент из стека"""
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Стек пуст")
            return None

    def peek(self):
        """Возвращает верхний элемент без удаления"""
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def is_empty(self):
        """Проверка на пустоту"""
        return len(self.items) == 0

    def find_extreme(self, find_max=True):
        """Находит максимальный или минимальный элемент в стеке"""
        if self.is_empty():
            print("Стек пуст")
            return None
        return max(self.items) if find_max else min(self.items)

    def display(self):
        """Показать содержимое стека"""
        print("Стек:", self.items)


