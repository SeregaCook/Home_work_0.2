# ===== Задание 3: Геометрические фигуры =====

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def get_area(self):
        pass

    def info(self):
        print(f"Фигура цвета: {self.color}")


class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def get_area(self):
        return math.pi * (self.radius ** 2)

    def info(self):
        super().info()
        print(f"Круг с радиусом {self.radius}, площадь: {self.get_area():.2f}")


class Square(Shape):
    def __init__(self, color, side):
        super().__init__(color)
        self.side = side

    def get_area(self):
        return self.side ** 2

    def info(self):
        super().info()
        print(f"Квадрат со стороной {self.side}, площадь: {self.get_area():.2f}")


# Демонстрация
circle = Circle("Синий", 5)
square = Square("Красный", 4)

circle.info()
square.info()
