# Вариант 1
#Из списка: ['Валентин', 'Петр', 'Анна', 'Евгений', 'Константин', 'Валерия',
#'Юлия'] получить новый список, в котором длина слов не превышает 5 символов.

def get_word_length(word):
    return len(word)

# фильтрации слов по длине
def filter_words_by_length(words, max_length):
    return list(filter(lambda word: get_word_length(word) <= max_length, words))

names = ['Валентин', 'Петр', 'Анна', 'Евгений', 'Константин', 'Валерия', 'Юлия']

# фильтруем список имен по длине слов, не превышающей 5 символов
filtered_names = filter_words_by_length(names, 5)

print(' '.join(filtered_names))