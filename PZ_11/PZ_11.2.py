#Вариант 1
#Из предложенного текстового файла (text18-1.txt) вывести на экран его содержимое,
#количество букв в верхнем регистре. Сформировать новый файл, в который поместить текст
#в стихотворной форме предварительно поставив последнюю строку между первой и второй.
with open("text18-1.txt", "r", encoding='utf-16') as file:
    #содержимое файла и выводим его на экран
    content = file.read()
    print("Содержимое файла:")
    print(content)

    #количество букв в верхнем регистре
    upper_count = sum(1 for char in content if char.isupper())
    print("Количество букв в верхнем регистре:", upper_count)

#разделение на строки
lines = content.splitlines()

#последняя строка между первой и второй
lines.insert(1, lines.pop())

#новый текст
new_content = "\n".join(lines)

#новый файл для записи
with open("new_text18-1.txt", "w", encoding='utf-16') as file:
    #записываем новый текст в файл
    file.write(new_content)

print("Новый файл создан: new_text18-1.txt")