#Даны два целых числа А и В (А < В). Вывести в порядке возрастания все целые числа,
#расположенные между А и В (включая сами числа А и В), а также количество N этих чисел.

a = input("Введите число a: ")
while type(a) != int:
    try:
        a = int(a)
    except ValueError:
        print('Ошибка ввода, повторите заново')
        a = input("Введите целое число: ")
b = input("Введите число b: ")
while type(b) != int:
    try:
        b = int(b)
    except ValueError:
        print('Ошибка ввода, повторите заново')
        b = input("Введите целое число: ")
if a >= b:
    print("Ошибка! Число b должно быть больше числа a")
else:
    n = 0
    for i in range(a, b + 1):
        print(i)
        n += 1
    print("Количество чисел:", n)