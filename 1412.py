#2 уровень убираем def taskN(): вставляем код
def task7():
    import random
    
    def my_max(arr):
        cur_max = arr[0]
        for x in arr: cur_max = x if x > cur_max else cur_max 
        return cur_max 
        
    matrix, result = [[random.randint(-10, 10) for _ in range(3)] for _ in range(5)], []
    
    print('Первоначальная матрица:')
    for r in matrix: print("".join(f"{elem:8d}" for elem in r))
    
    for row in matrix:
        print('Текущий ряд')
        print(*row)
        print(f'Максимальный элемент: {my_max(row)}\n')
        result.append(my_max(row))
    
    print('Полученный массив: ')
    print(*result)

def task10():
    import random

    matrix, cur_max, cur_ind = [[random.randint(-10, 10) for _ in range(5)] for _ in range(7)], float('-inf'), 0
    
    print('Первоначальная матрица:')
    for r in matrix: print("".join(f"{elem:8d}" for elem in r))
    
    for row in range(len(matrix)):
        if matrix[row][2] > cur_max: 
            cur_max = matrix[row][2]
            cur_ind = row 
    
    print(f'Номер строки {cur_ind + 1}, сама строка: {matrix[cur_ind]}, сам элемент {matrix[cur_ind][2]}')
    
    matrix[cur_ind], matrix[3] = matrix[3], matrix[cur_ind]
    print('Полученная матрица:')
    for r in matrix: print("".join(f"{elem:8d}" for elem in r))
    
def task23():
    import random

    def my_max(arr):
        cur_max = arr[0]
        for x in arr: cur_max = x if x > cur_max else cur_max 
        return cur_max 
    
    H = [[random.randint(-10, 10) for _ in range(6)] for _ in range(5)]
    
    print('Первоначальная матрица:')
    for r in H: print("".join(f"{elem:8}" for elem in r))

    for i in range(5):
        max_value = my_max(H[i]) 
        max_index = H[i].index(max_value) 
        H[i].insert(max_index + 1, max_value)  

    print('Полученная матрица:')
    for r in H: print("".join(f"{elem:8}" for elem in r))

def task40():
    import random

    def my_max(arr):
        cur_max = arr[0]
        for x in arr: cur_max = x if x > cur_max else cur_max 
        return cur_max 
    
    size = 6
    
    A = [[random.randint(-10, 10) for _ in range(size)] for _ in range(size)]
    
    print('Первоначальная матрица:')
    for r in A: print("".join(f"{elem:8}" for elem in r))
    
    max_element = None
    max_index = -1
    for i in range(size):
        if max_element is None or A[i][i] > max_element:
            max_element = A[i][i]
            max_index = i
            
    print(f"\nМаксимальный элемент на главной диагонали: {max_element} (в строке {max_index})")

    for i in range(max_index):
        for j in range(i + 1, size):
            A[i][j] = 0
    
    print('Полученная матрица:')
    for r in A: print("".join(f"{elem:8}" for elem in r))
#3 уровень
import random

def task2_od():
    y = int(input("Введите длину массива: "))
    arr = [random.randint(-10, 10) for _ in range(y)]
    print("Массив:")
    print(*arr)

    add_up, max_el = 1, max(arr)
    for i in range(len(arr)):
        if arr[i] == max_el:
            arr[i] += add_up
            add_up += 1

    print("Результат массива:")
    print(*arr)

def task2_ma():
    x = int(input("Введите высоту матрицы: "))
    y = int(input("Введите длину матрицы: "))
    matrix = [[random.randint(-1, 1) for _ in range(y)] for _ in range(x)]
    print("Матрица:")
    for row in matrix:
        print(" ".join(f"{el:8.2f}" for el in row))

    add_up = 1
    for row in matrix:
        max_el = max(row)
        for i in range(len(row)):
            if row[i] == max_el:
                row[i] += add_up
                add_up += 1

    print("Результат матрицы:")
    for row in matrix:
        print(" ".join(f"{el:8.2f}" for el in row))

import random

def task6_od():
    y = int(input("Введите длину массива: "))
    arr = [random.randint(-10, 10) for _ in range(y)]
    print("Массив:")
    print(*arr)
    max_length = 0
    cur_length = 1
    for i in range(1, len(arr)):
        if arr[i - 1] > arr[i]:
            cur_length += 1
        else:
            max_length = max(max_length, cur_length)
            cur_length = 1
    max_length = max(max_length, cur_length)
    print(f"Максимальная длина убывающей последовательности: {max_length}")

def task6_ma():
    import random

    x, y = map(int, input("Введите высоту и длину матрицы через пробел: ").split())
    matrix = [[random.randint(-10, 10) for _ in range(y)] for _ in range(x)]

    print("Первоначальная матрица:")
    for row in matrix:
        print(" ".join(f"{el:8.2f}" for el in row))

    max_length, sequences, indexes = 0, [], []

    for row_index, row in enumerate(matrix):
        cur_length, current_sequence = 1, [row[0]]

        for i in range(1, len(row)):
            if row[i - 1] > row[i]:
                cur_length += 1
                current_sequence.append(row[i])
            else:
                if cur_length > max_length:
                    max_length = cur_length
                    sequences = [current_sequence.copy()]
                    indexes = [row_index + 1]
                elif cur_length == max_length:
                    sequences.append(current_sequence.copy())
                    indexes.append(row_index + 1)
                cur_length, current_sequence = 1, [row[i]]

        if cur_length > max_length:
            max_length = cur_length
            sequences = [current_sequence.copy()]
            indexes = [row_index + 1]
        elif cur_length == max_length:
            sequences.append(current_sequence.copy())
            indexes.append(row_index + 1)

    if max_length > 1:
        formatted_sequences = ', '.join(f"({' '.join(map(str, seq))})" for seq in sequences)
        print(f"Результат: {max_length}, номера строк ({', '.join(map(str, set(indexes)))}), элементы {formatted_sequences}")
    else:
        print("Не найдены увеличивающиеся последовательности.")

def task14_odnomerniy():
    import random
    def my_max(arr):
        max_elem = float('-inf')
        for x in arr:
            if x > max_elem:
                max_elem = x
        return max_elem
    length = int(input('Введите длину массива: '))
    arr = [random.randint(-100, 100) for _ in range(length)]

    max_value = my_max(arr)
    divider = 10 ** (len(str(max_value)) + 1)
    
    print('Первоначальный массив:', *arr)

    arr_transformed = [x / divider for x in arr]
    print('Преобразованный массив:', *arr_transformed)

    arr_reverted = [int(x * divider) for x in arr_transformed]
    print('Возвращённый массив:', *arr_reverted)


def task14_dvumerniy():
    import random
    def my_max(arr):
        max_elem = float('-inf')
        for x in arr:
            if x > max_elem:
                max_elem = x
        return max_elem
    
    def my_max_matrix(matrix):
        return my_max(my_max(abs(x) for x in row) for row in matrix)

    rows = int(input('Введите количество строк: '))
    cols = int(input('Введите количество столбцов: '))

    matrix = [[random.randint(-100, 100) for _ in range(cols)] for _ in range(rows)]

    max_value = my_max_matrix(matrix)
    divider = 10 ** (len(str(max_value)) + 1)
    
    print('Первоначальная матрица:')
    for row in matrix:
        print("".join(f"{elem:8}" for elem in row))

    matrix_transformed = [[x / divider for x in row] for row in matrix]
    print('Преобразованная матрица:')
    for row in matrix_transformed:
        print("".join(f"{elem:8}" for elem in row))

    matrix_reverted = [[int(x * divider) for x in row] for row in matrix_transformed]
    print('Возвращённая матрица:')
    for row in matrix_reverted:
        print("".join(f"{elem:8}" for elem in row))
