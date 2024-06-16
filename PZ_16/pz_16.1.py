# Вариант 1
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def circumference(self):
        return 2 * 3.14 * self.radius

    def diameter(self):
        return 2 * self.radius

circle = Circle(5)

print(f'Площадь круга: {circle.area()}')

print(f'Длина окружности круга: {circle.circumference()}')

print(f'Диаметр круга: {circle.diameter()}')