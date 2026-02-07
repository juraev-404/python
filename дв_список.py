from datetime import datetime

class Reminder:
    def __init__(self, message, offset):
        self.message = message
        self.offset = offset  # timedelta

    def __repr__(self):
        return f"Reminder(message='{self.message}', offset={self.offset})"

class TaskNode:
    def __init__(self, title, description, start_date, end_date, reminders=None):
        self.title = title
        self.description = description
        self.start_date = start_date 
        self.end_date = end_date    
        self.reminders = reminders if reminders else []
        self.prev = None
        self.next = None

    def __repr__(self):
        return (f"TaskNode(title='{self.title}', start={self.start_date}, end={self.end_date}, "
                f"reminders={self.reminders})")

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_task(self, task):
        if not self.head:
            self.head = self.tail = task
        else:
            self.tail.next = task
            task.prev = self.tail
            self.tail = task

    def display_tasks(self):
        current = self.head
        while current:
            print(current)
            current = current.next

# Пример использования
if __name__ == "__main__":
    from datetime import timedelta

    task1 = TaskNode(
        title="Сдать отчёт",
        description="Подготовить и сдать финансовый отчёт",
        start_date=datetime(2025, 4, 25, 10, 0),
        end_date=datetime(2025, 4, 25, 12, 0),
        reminders=[
            Reminder("Напоминание за 1 день", timedelta(days=-1)),
            Reminder("Напоминание за 1 час", timedelta(hours=-1))
        ]
    )

    task2 = TaskNode(
        title="Встреча с командой",
        description="Еженедельная синхронизация с командой проекта",
        start_date=datetime(2025, 4, 26, 9, 0),
        end_date=datetime(2025, 4, 26, 10, 0),
        reminders=[
            Reminder("Напоминание за 30 минут", timedelta(minutes=-30))
        ]
    )

    calendar = DoublyLinkedList()
    calendar.add_task(task1)
    calendar.add_task(task2)

    calendar.display_tasks()
