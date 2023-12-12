#Дан список размера N. Найти номера тех элементов списка, которые больше своего
#правого соседа, и количество таких элементов. Найденные номера выводить
#в порядке их возрастания.
def find_larger_elements(arr):
    result = []
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            result.append(i)
    return result, len(result)

if __name__ == "__main__":
    input_list = [3, 5, 1, 6, 2, 7, 9, 8]
    indices, count = find_larger_elements(input_list)
    if count == 0:
        print("Нет элементов, больше своего правого соседа.")
    else:
        print("Найдены следующие элементы, больше своего правого соседа:")
        for index in indices:
            print(f"Элемент в позиции {index} равен {input_list[index]}")
        print(f"Количество таких элементов: {count}")