#Вариант 1
#Перенести в новую матрицу Matr1 элементы, которые не находятся в первых и
#последних строках и столбцах матрицы Matr2 произвольного размера.

Matr2 = [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12],
         [13, 14, 15, 16]]

def create_new_matrix(matrix):
    new_matrix = [row[1:-1] for row in matrix[1:-1]]
    return new_matrix


Matr1 = create_new_matrix(Matr2)

for row in Matr1:
    print(row)