#СДЕЛАНЫ ЗАДАНИЯ:
#3,8,9,12,25,34,42
#
# удаляем
# def taskN():
# ...
# taskN()
#
#
#вспомогательная функция чтобы выводить матрицы 
def show_matrix(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print("{:8.2f}".format(arr[i][j]), end="")
        print()
        print()


#вспомогательная функция для создания рандомной матрицы x - высота, y - длина
def create_matrix(x, y):
    import random 
    matrix = [[]] * x
    for i in range(len(matrix)): 
        matrix[i] = [random.randint(-100,100) for _ in range(y)]
    return matrix 

#2 уровень
#3. Найти след (сумму диагональных элементов) квадратной матрицы А 
#размером 4 × 4).

def task_3(): 
    x = int(input('Введите высоту матрицы: '))
    y = int(input('Введите длину матрицы: '))

    if x != y: 
        print('Матрица не квадрантая, пожалуйста введите правильные значения')
        task_3()

    matrix, result = create_matrix(x, y), 0

    print(f'Первоначальная матрица:')
    show_matrix(matrix)

    for i in range(len(matrix)):
        result += matrix[i][i]
        print(f'Текущий элемент: {matrix[i][i]}, результат сейчас: {result}')
    
    return f'Ответ: {result}'
#print(task_3())

#8. Сформировать одномерный массив из средних значений среди 
#положительных элементов строк матрицы А размером 4 × 6.
 
def task_8():
    x = int(input('Введите высоту матрицы: '))
    y = int(input('Введите длину матрицы: '))

    matrix, result = create_matrix(x, y), []

    print(f'Первоначальная матрица:')
    show_matrix(matrix)

    for row in matrix:
        lst_of_positives = [x for x in row if x > 0]
        print(f'Текущий ряд: {row}, положительные числа: {lst_of_positives}')
        print(f'Среднее значение: {sum(lst_of_positives) // len(lst_of_positives)}')
        result.append(sum(lst_of_positives) // len(lst_of_positives))
    
    print('Ответ:')
    print(*result)
#print(task_8())

def task9():
    import random

    def my_max(arr):
        current_max = arr[0]
        for x in arr:
            if current_max < x:
                current_max = x
        return current_max
 
    matrix = [[0] * 7 for _ in range(5)]


    for i in range(5): 
        for j in range(7):
            matrix[i][j] = random.randint(-10, 10)

    print('Первоначальная матрица')
    for z in range(5):
        for y in range(7):
            print("{:4}".format(matrix[z][y]), end="")
        print()

    for a in range(5):
        biggest_elem = my_max(matrix[a])
        print(f'Наибольший элемент {biggest_elem}, первый элемент {matrix[a][0]}')
        if biggest_elem != matrix[a][0]:
            biggest_elem_index = matrix[a].index(biggest_elem)
            matrix[a][biggest_elem_index], matrix[a][0] = matrix[a][0], biggest_elem
        print(f'Ряд сейчас {matrix[a]}')
        print()
    
    print('Результат')
    for z in range(5):
        for y in range(7):
            print("{:4}".format(matrix[z][y]), end="")
        print()
#task9()

#12. В матрице А размером 6 × 7 удалить столбец и строку, на пересечении 
#которых находится максимальный элемент матрицы. 

def task_12():
    x = int(input('Введите высоту матрицы: '))
    y = int(input('Введите длину матрицы: '))

    matrix = create_matrix(x, y)
    print('Первоначальная матрица:')
    show_matrix(matrix)

    max_elem = matrix[0][0]
    max_indx = [0, 0]

    for i in range(x):
        for j in range(y):
            if matrix[i][j] > max_elem:
                max_elem, max_indx = matrix[i][j], [i, j]
    
    print(f'Максимальный элемент матрицы: {max_elem}, он находится на a{max_indx[0]}{max_indx[1]}')

    del matrix[max_indx[0]]
    
    for row in matrix:
        del row[max_indx[1]]

    print('Матрица после удаления строки и столбца:')
    show_matrix(matrix)
#task_12()

def task18():
    import random

    n = int(input('Введите высоту матрицы: '))
    m = int(input('Введите длину матрицы: '))

    matrix = [[0] * m for _ in range(n)]

    for i in range(n): 
        for j in range(m):
            matrix[i][j] = random.randint(-10, 10)

    print('Первоначальная матрица')
    for z in range(n):
        for y in range(m):
            print("{:4}".format(matrix[z][y]), end="")
        print()

    for a in range(n):
        print(f'Ряд на начало: {matrix[a]}')
        
        max_elem = None
        last_index = -1
        
        for i in range(len(matrix[a])):
            if matrix[a][i] < 0:
                last_index = i
                break
            if max_elem is None or matrix[a][i] > max_elem:
                max_elem = matrix[a][i]

        if max_elem is not None and last_index != -1:
            print(f'Наибольший перед отрицательным {max_elem}, последний отрицательный {matrix[a][last_index]}')
            max_index = matrix[a].index(max_elem)
            matrix[a][max_index], matrix[a][last_index] = matrix[a][last_index], matrix[a][max_index]
        else: 
            print('Нет отрицательных или отрицательный первое.')
        print(f'Ряд сейчас {matrix[a]}')
        print()

    print('Результат:')
    for z in range(n):
        for y in range(m):
            print("{:4}".format(matrix[z][y]), end="")
        print()
#task18()

def task25(): # ЕСЛИ КОЛ-ВО ОТРИЦАТЕЛЬНЫХ ЧИСЕЛ ОДИНАКОВОЕ, ЗДЕСЬ НАХОДИМ ТОЛЬКО ПЕРВУЮ МАКСИМАЛЬНУЮ СТРОКУ И ПЕРВУЮ МИНИМАЛЬНУЮ
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
            if current_min < x:
                current_min = x
        return current_min

    n = 6  
    m = 5  

    matrix = [[0] * m for _ in range(n)]

    for i in range(n): 
        for j in range(m):
            matrix[i][j] = random.randint(-10, 10)

    print('Первоначальная матрица')
    for z in range(n):
        for y in range(m):
            print("{:4}".format(matrix[z][y]), end="")
        print()

    neg_counts = []
    for a in range(n):
        cur_neg_count = 0
        for x in matrix[a]:
            if x < 0:
                cur_neg_count += 1
        neg_counts.append(cur_neg_count)
        print(f'Ряд сейчас: {matrix[a]}, количество отрицательных чисел: {cur_neg_count}')

    max_value = my_max(neg_counts)
    min_value = my_min(neg_counts)

    max_indices = [i for i, count in enumerate(neg_counts) if count == max_value]
    min_indices = [i for i, count in enumerate(neg_counts) if count == min_value]

    if max_indices and min_indices:
        matrix[min_indices[0]], matrix[max_indices[0]] = matrix[max_indices[0]], matrix[min_indices[0]]


    print('Результат:')
    for z in range(n):
        for y in range(m):
            print("{:4}".format(matrix[z][y]), end="")
        print()
#task25()

#34. Дана матрица A размером 5 × 7. Для каждой строки сравнить элементы, 
#расположенные непосредственно перед и после максимального 
#элемента этой строки, и меньший из них увеличить в 2 раза. Если 
#максимальный элемент является первым или последним в строке, то 
#увеличить в 2 раза только один соседний с максимальным элемент.

def task_34():
    def my_max(arr):
        max_elem = float('-inf')
        for x in arr:
            max_elem = x if x > max_elem else max_elem
        return max_elem 

    def my_min(arr):
        min_elem = float('inf')
        for x in arr:
            min_elem = x if x < min_elem else min_elem
        return min_elem

    x = int(input('Введите высоту матрицы: '))
    y = int(input('Введите длину матрицы: '))

    matrix = create_matrix(x, y)
    print('Первоначальная матрица:')
    show_matrix(matrix)

    for j in range(x):
        max_element = my_max(matrix[j])
        max_index = matrix[j].index(max_element)
        print(f'Ряд номер {j + 1}: {matrix[j]}, наибольший элемент: {max_element}')
        if max_index == 0:   
            print(f'Элемент {matrix[j][max_index + 1]}, удваивается')
            if matrix[j][max_index + 1] < 0:
                matrix[j][max_index + 1] /= 2
            else: 
                matrix[j][max_index + 1] *= 2
            print(f'Полученный ряд: {matrix[j]}\n')
        elif max_index == y - 1: 
            print(f'Элемент {matrix[j][max_index - 1]}, удваивается')
            if matrix[j][max_index - 1] < 0:
                matrix[j][max_index - 1] /= 2 
            else: 
                matrix[j][max_index - 1] *= 2
            print(f'Полученный ряд: {matrix[j]}\n')
        else:
            print(f'Сравниваем элементы: {matrix[j][max_index - 1]} и {matrix[j][max_index + 1]}')
            if matrix[j][max_index - 1] < matrix[j][max_index + 1]:
                print(f'Так как элемент {matrix[j][max_index - 1]} меньше, он удваивается')
                if matrix[j][max_index - 1] < 0:
                    matrix[j][max_index - 1] /= 2
                else: 
                    matrix[j][max_index - 1] *= 2
                print(f'Полученный ряд: {matrix[j]}\n')
            else: 
                print(f'Так как элемент {matrix[j][max_index + 1]} меньше, он удваивается')
                if matrix[j][max_index + 1] < 0 : 
                    matrix[j][max_index + 1] /= 2
                else: 
                    matrix[j][max_index + 1] *= 2
                print(f'Полученный ряд: {matrix[j]}\n')
    print('Ответ:')
    show_matrix(matrix)
#task_34()

def task42(): 
    import random

    n = 6  
    m = 7  

    matrix = [[0] * m for _ in range(n)]

    for i in range(n): 
        for j in range(m):
            matrix[i][j] = random.randint(-10, 10)

    print('Первоначальная матрица')
    for z in range(n):
        for y in range(m):
            print("{:4}".format(matrix[z][y]), end="")
        print()

    for a in range(n):
        print(f'Ряд в начале: {matrix[a]}')
        matrix[a] = matrix[a][::-1]
        print(f'Ряд сейчас: {matrix[a]}')
        print()

    print('Результат:')
    for z in range(n):
        for y in range(m):
            print("{:4}".format(matrix[z][y]), end="")
        print()
#task42()
