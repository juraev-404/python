from datetime import datetime

class Task:
    def __init__(self, title, description, start_date, end_date, reminders=None):
        self.title = title  # Название задачи
        self.description = description  # Описание
        self.start_date = start_date  # datetime объект
        self.end_date = end_date  # datetime объект
        self.reminders = reminders if reminders else []  # Список напоминаний (timedelta или текст)
        self.prev = None  # Указатель на предыдущую задачу
        self.next = None  # Указатель на следующую задачу

    def __str__(self):
        return f"{self.title} ({self.start_date.strftime('%Y-%m-%d %H:%M')} - {self.end_date.strftime('%Y-%m-%d %H:%M')})"


class TaskCalendar:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_task(self, task):
        if self.head is None:
            self.head = self.tail = task
        else:
            self.tail.next = task
            task.prev = self.tail
            self.tail = task

    def display_forward(self):
        current = self.head
        while current:
            print(current)
            print(f"  Описание: {current.description}")
            print(f"  Напоминания: {current.reminders}")
            current = current.next

    def display_backward(self):
        current = self.tail
        while current:
            print(current)
            print(f"  Описание: {current.description}")
            print(f"  Напоминания: {current.reminders}")
            current = current.prev


# Пример использования:
calendar = TaskCalendar()

task1 = Task(
    "Подготовка отчета",
    "Собрать все данные и составить отчет",
    datetime(2025, 6, 5, 10, 0),
    datetime(2025, 6, 6, 18, 0),
    reminders=["за день до окончания", "за час до начала"]
)

task2 = Task(
    "Встреча с клиентом",
    "Обсудить детали проекта",
    datetime(2025, 6, 7, 15, 0),
    datetime(2025, 6, 7, 16, 0),
    reminders=["за 2 часа до начала"]
)

calendar.add_task(task1)
calendar.add_task(task2)

print("Задачи по порядку:")
calendar.display_forward()

