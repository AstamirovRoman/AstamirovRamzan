#Вариант 1
#Даны координаты точки, не лежащей на координатных осях ox и oy.
#Определить номер координатной четверти, в которой находится данная точка.

x = input("Введите координату x: ")
while type(x) != float:
    try:
        x = float(x)
    except ValueError:
        print('Ошибка ввода, повторите заново')
        x = input("Введите координату x: ")
y = input("Введите координату y: ")
while type(y) != float:
    try:
        y = float(y)
    except ValueError:
        print('Ошибка ввода, повторите заново')
        y = input("Введите координату y: ")

if x > 0 and y > 0:
    print("Точка находится в первой координатной четверти")
elif x < 0 and y > 0:
    print("Точка находится во второй координатной четверти")
elif x < 0 and y < 0:
    print("Точка находится в третьей координатной четверти")
elif x > 0 and y < 0:
    print("Точка находится в четвертой координатной четверти")
else:
    print("Точка лежит на одной из осей")