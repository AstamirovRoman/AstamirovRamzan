import pickle

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def circumference(self):
        return 2 * 3.14 * self.radius

    def diameter(self):
        return 2 * self.radius

# Создаем три объекта класса Круг
circle1 = Circle(5)
circle2 = Circle(7)
circle3 = Circle(10)

# Сохраняем информацию в файл
def save_def(circles, filename):
    with open(filename, 'wb') as f:
        pickle.dump(circles, f)

# Загружаем информацию из файла
def load_def(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)

# Сохраняем информацию в файл
save_def([circle1, circle2, circle3], 'circles.pkl')

# Загружаем информацию из файла
loaded_circles = load_def('circles.pkl')

# Выводим информацию о загруженных кругах
for circle in loaded_circles:
    print(f'Площадь круга: {circle.area()}')
    print(f'Длина окружности круга: {circle.circumference()}')
    print(f'Диаметр круга: {circle.diameter()}')
    print()
