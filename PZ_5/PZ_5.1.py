#Вариант 1
#Составить функцию решения задачи: из заданного числа вычли сумму его цифр.
# Из результата вновь вычли сумму его цифр и т. д. Через сколько таких действий получится нуль?
def subtract_digits(a):
    n = 0
    while a != 0:
        digit_sum = sum(int(digit) for digit in str(a))
        a -= digit_sum
        n += 1
    return n

a = int(input("Введите число: "))
result = subtract_digits(a)
print(f"Количество действий: {result}")