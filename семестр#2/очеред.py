class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, value):
        """Добавляет элемент в конец очереди"""
        self.items.append(value)

    def dequeue(self):
        """Удаляет элемент из начала очереди и возвращает его"""
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("Очередь пуста")
            return None

    def sort(self):
        """Сортирует элементы очереди по возрастанию"""
        self.items.sort()

    def is_empty(self):
        """Проверяет, пуста ли очередь"""
        return len(self.items) == 0

    def peek(self):
        """Возвращает первый элемент очереди без удаления"""
        if not self.is_empty():
            return self.items[0]
        else:
            return None

    def display(self):
        """Выводит все элементы очереди"""
        print("Очередь:", self.items)

