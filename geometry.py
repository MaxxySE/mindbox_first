from abc import ABC, abstractmethod
import math


# area - высчитывается площадь фигуры
# is_right - проверка фигуры на прямоугольность

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def is_right(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def is_right(self):
        return False  # Круг не может быть прямоугольным


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def is_right(self):
        sides = sorted([self.a, self.b, self.c])
        return math.isclose(sides[0] ** 2 + sides[1] ** 2, sides[2] ** 2)


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def is_right(self):
        return True  # Все углы квадрата прямые


def calculate_area(shape: Shape):
    return shape.area()

# Для удобства можно было бы вынести классы фигур по разным файлам, если в будущем планируется добавлять новые
# Однако, поскольку у нас только две фигуры, принял решение, что проще и быстрее для проверки будет сделать так
