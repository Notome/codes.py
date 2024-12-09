#14 одномерный
import random

y = int(input('Введите длину массива: '))
arr = [random.randint(-10, 10) for _ in range(y)]
max_elem = max(arr)
magical_number = int('1' + (len(str(max_elem)) * '0'))

print('Первоначальный массив:')
print(', '.join(map(str, arr)))

for i in range(len(arr)):
    arr[i] /= magical_number

print('Преобразованный массив:')
print(', '.join(map(str, arr)))

for i in range(len(arr)):
    arr[i] = int(arr[i] * magical_number)

print('Возвращаем массив в обычное состояние:')
print(', '.join(map(str, arr)))
#14 двумерный 
import random

x = int(input('Введите высоту матрицы: '))
y = int(input('Введите длину матрицы: '))
matrix = [[random.randint(-10, 10) for _ in range(y)] for _ in range(x)]
max_elem = max(max(row) for row in matrix)
magical_number = int('1' + (len(str(max_elem)) * '0'))

print('Первоначальная матрица:')
for row in matrix:
    print(", ".join(f"{elem:8.2f}" for elem in row))

for i in range(x):
    for j in range(y):
        matrix[i][j] /= magical_number

print('Преобразованная матрица:')
for row in matrix:
    print(", ".join(f"{elem:8.2f}" for elem in row))

for i in range(x):
    for j in range(y):
        matrix[i][j] = int(matrix[i][j] * magical_number)

print('Возвращаем матрицу в обычное состояние:')
for row in matrix:
    print(", ".join(f"{elem:8d}" for elem in row))

#25 задание 
import random

def my_max(arr):
    current_max = arr[0]
    for x in arr:
        if current_max < x:
            current_max = x
    return current_max

def my_min(arr):
    current_min = arr[0]
    for x in arr:
        if current_min > x:
            current_min = x
    return current_min

n = 6  
m = 5  

matrix = [[random.randint(-10, 10) for _ in range(m)] for _ in range(n)]

print('Первоначальная матрица:')
for row in matrix:
    print("".join(f"{elem:4}" for elem in row))

neg_counts = []
for row in matrix:
    cur_neg_count = sum(1 for x in row if x < 0)
    neg_counts.append(cur_neg_count)
    print(f'Ряд сейчас: {row}, количество отрицательных чисел: {cur_neg_count}')

max_value = my_max(neg_counts)
min_value = my_min(neg_counts)

max_indices = [i for i, count in enumerate(neg_counts) if count == max_value]
min_indices = [i for i, count in enumerate(neg_counts) if count == min_value]

if max_indices and min_indices:
    matrix[min_indices[0]], matrix[max_indices[0]] = matrix[max_indices[0]], matrix[min_indices[0]]

print('Результат:')
for row in matrix:
    print("".join(f"{elem:4}" for elem in row))
