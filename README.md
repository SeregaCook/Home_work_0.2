class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        # Приватный атрибут (инкапсуляция)
        self.__is_borrowed = False

    def borrow(self):
        if not self.__is_borrowed:
            self.__is_borrowed = True
            return True
        return False

    def return_book(self):
        self.__is_borrowed = False

    def get_info(self):
        status = "Выдана" if self.__is_borrowed else "Доступна"
        return f"Название: {self.title}, Автор: {self.author}, Год: {self.year}, Статус: {status}"


class EBook(Book):
    def __init__(self, title, author, year, file_size: float):
        super().__init__(title, author, year)
        self.file_size = file_size

    def get_info(self):
        # Полиморфизм: расширяем базовый метод
        base_info = super().get_info()
        return f"{base_info}, Размер файла: {self.file_size}MB"

    def borrow(self):
        # Электронная книга всегда доступна (логика из задания)
        # Устанавливаем статус в True (имитация аренды), но всегда возвращаем True
        self._Book__is_borrowed = True 
        return True


class AudioBook(Book):
    def __init__(self, title, author, year, duration: int, narrator: str):
        super().__init__(title, author, year)
        self.duration = duration
        self.narrator = narrator

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Чтец: {self.narrator}, Длительность: {self.duration} мин."

    def __str__(self):
        # Магический метод для краткого вывода
        return f"Аудиокнига: {self.title} - {self.narrator}"

    def __eq__(self, other):
        # Сравнение двух аудиокниг
        if not isinstance(other, AudioBook):
            return False
        return (self.title == other.title and 
                self.author == other.author and 
                self.narrator == other.narrator)

# --- Пример использования ---

# 1. Создаем обычную книгу
paper_book = Book("Преступление и наказание", "Ф. Достоевский", 1866)
print(paper_book.get_info())
print(f"Берем книгу: {paper_book.borrow()}")
print(f"Повторно берем ту же книгу: {paper_book.borrow()}") # Должно быть False

# 2. Создаем электронную книгу
kindle_book = EBook("Цифровая крепость", "Дэн Браун", 1998, 1.5)
print(kindle_book.get_info())
print(f"Берем e-book: {kindle_book.borrow()}") # Всегда True

# 3. Создаем аудиокниги и сравниваем их
audio1 = AudioBook("Хоббит", "Дж. Толкин", 1937, 600, "А. Клюквин")
audio2 = AudioBook("Хоббит", "Дж. Толкин", 1937, 600, "А. Клюквин")

print(audio1) # Вызов __str__
print(f"Книги одинаковые? {audio1 == audio2}") # Вызов __eq__
