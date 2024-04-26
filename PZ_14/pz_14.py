import re

def count_surnames(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        surnames = re.findall(r'\b[A-ZА-Я][a-zа-я]+(?:-[A-ZА-Я][a-zа-я]+)?\b', text)
        return len(surnames)

def replace_word(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        new_text = re.sub(r'\bроман\b', 'произведение', text)

    with open('new_file.txt', 'w', encoding='utf-8') as new_file:
        new_file.write(new_text)

file_path = 'writer.txt'
surname_count = count_surnames(file_path)
print(f'Количество фамилий писателей: {surname_count}')
replace_word(file_path)
print('Замена выполнена. Результат сохранен в new_file.txt')