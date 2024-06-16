# Вариант 1
class Figure:
    def area(self):
        pass

class Square(Figure):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Rectangle(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


square = Square(5)
print(f'Площадь квадрата: {square.area()}')

rectangle = Rectangle(4, 6)
print(f'Площадь прямоугольника: {rectangle.area()}')
