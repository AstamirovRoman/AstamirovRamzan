#Дана строка, содержащая латинские буквы и скобки трех видов: «)», «», «3». Если скобки
#расставлены правильно (то есть каждой открывающей соответствует закрывающая скобка того же вида),
#то вывести число 0. В противном случае вывести или номер позиции, в которой расположена
#первая ошибочная скобка, или, если закрывающих скобок не хватает, число —1.
S = input('Введите строку: ')
i = 0
error = 0
num1 = 0
num2 = 0
num3 = 0

while i < len(S):
    if S[i] == '(':
        num1 += 1
    elif S[i] == ')':
        num1 -= 1
    elif S[i] == '[':
        num2 += 1
    elif S[i] == ']':
        num2 -= 1
    elif S[i] == '{':
        num3 += 1
    elif S[i] == '}':
        num3 -= 1

    if (num1 < 0 or num2 < 0 or num3 < 0) and error == 0:
        error = i + 1
    i += 1

if error != 0:
    print(error)
elif num1 > 0 or num2 > 0 or num3 > 0:
    print(-1)
else:
    print(0)