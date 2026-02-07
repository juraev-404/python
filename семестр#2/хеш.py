# а) Создать класс «Книга» с полями «Название», «Автор», «Год выпуска» и 
# «Количество страниц». Создать хеш-таблицу для хранения объектов класса 
# «Книга» по ключу — ISBN. 
# б) Написать функцию для нахождения количества элементов из хеш
# таблицы, у которых значение больше заданного значения. 
# в) Реализуйте хеш-таблицу для хранения информации о товарах на складе. 
# Ключом является штрих-код товара, значение — объект, содержащий 
# информацию о товаре (название, количество, цена и т.д.). Используйте метод 
# разрешения коллизий методом цепочек. 

# a 
class Book:
    def __init__(self, title, author, year, pages):
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages

    def __str__(self):
        return f"{self.title} ({self.author}, {self.year}) - {self.pages} стр."

# Хеш-таблица: ключ — ISBN, значение — объект Book
books_by_isbn = {}

# Пример добавления книг
books_by_isbn["978-5-699-12014-5"] = Book("Преступление и наказание", "Ф. М. Достоевский", 1866, 670)
books_by_isbn["978-0-14-044926-6"] = Book("Война и мир", "Л. Н. Толстой", 1869, 1225)
books_by_isbn["978-0-14-044793-4"] = Book("Анна Каренина", "Л. Н. Толстой", 1877, 963)

# б

def count_books_with_more_pages(book_table, min_pages):
    count = 0
    for book in book_table.values():
        if book.pages > min_pages:
            count += 1
    return count

# Пример использования:
print("Книг больше 800 страниц:", count_books_with_more_pages(books_by_isbn, 800))


# в

class Product:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"{self.name}: {self.quantity} шт., {self.price}₽"

class ProductHashTable:
    def __init__(self, size=10):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def add_product(self, barcode, product):
        index = self._hash(barcode)
        # проверим, есть ли такой ключ — обновим
        for i, (k, v) in enumerate(self.buckets[index]):
            if k == barcode:
                self.buckets[index][i] = (barcode, product)
                return
        self.buckets[index].append((barcode, product))

    def get_product(self, barcode):
        index = self._hash(barcode)
        for k, v in self.buckets[index]:
            if k == barcode:
                return v
        return None  # не найдено

    def __str__(self):
        result = []
        for i, bucket in enumerate(self.buckets):
            if bucket:
                for k, v in bucket:
                    result.append(f"[{k}] {v}")
        return "\n".join(result)
