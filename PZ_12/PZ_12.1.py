#Вариант 1
#Организовать и вывести последовательность А из n чисел. Из
#последовательности А получить две последовательности В и С: в последовательности В –
#четные элементы А, в С – нечетные элементы А. Произвести суммирование
#соответствующих элементов последовательностей В и С. Найти минимальный элемент
#полученной последовательности.

from functools import reduce

def create_sequence(n):
    return list(range(1, n + 1))

#  четные элементы последовательности
def get_even_elements(sequence):
    return [x for x in sequence if x % 2 == 0]

# нечетные элементы последовательности
def get_odd_elements(sequence):
    return [x for x in sequence if x % 2 != 0]

# суммирование соответствующих элементов двух последовательностей
def sum_corresponding_elements(sequence1, sequence2):
    return [x + y for x, y in zip(sequence1, sequence2)]

# поиск минимального элемента последовательности
def find_min(sequence):
    return reduce(min, sequence)

sequence = create_sequence(10)

# четные и нечетные элементы последовательности
even_elements = get_even_elements(sequence)
odd_elements = get_odd_elements(sequence)

# сумма соответствующих элементов четной и нечетной последовательностей
summed_elements = sum_corresponding_elements(even_elements, odd_elements)

# минимальный элемент полученной последовательности
min_element = find_min(summed_elements)


print(f"Последовательность A: {sequence}")
print(f"Четные элементы последовательности A: {even_elements}")
print(f"Нечетные элементы последовательности A: {odd_elements}")
print(f"Сумма соответствующих элементов четной и нечетной последовательностей: {summed_elements}")
print(f"Минимальный элемент полученной последовательности: {min_element}")