#убираем class и def
class lvl2():
    def task5():
        import random
        matrix = [[random.randint(-10, 10) for _ in range(5)] for _ in range(6)]
        print('Первоначальная матрица:')
        for r in matrix:
            print("".join(f"{elem:8d}" for elem in r))
        
        try:
            inp = int(input('Введите номер столбца (1-5): ')) - 1
            if inp < 0 or inp >= 5:
                raise ValueError("Номер столбца вне диапазона")

            for i in range(len(matrix)):
                if matrix[i][inp] < 0:
                    print(f'Первый отрицательный элемент находится на строке ({i+1}) и его значение равно {matrix[i][inp]}')
                    break
            else:
                print('Отрицательных элементов в выбранном столбце нет.')
        except ValueError as e:
            print('Введенное значение не верно:', e)
        except IndexError:
            print('Ошибка индекса, проверьте размер матрицы.')

    def task9():
        def my_max(arr):
            cur_max = arr[0]
            for x in arr: cur_max = x if x > cur_max else cur_max 
            return cur_max 
        import random
        matrix = [[random.randint(-10, 10) for _ in range(5)] for _ in range(7)]
        print('Первоначальная матрица:')
        for r in matrix:
            print("".join(f"{elem:8d}" for elem in r))
        for row in range(7):
            print(f'Текущий ряд {matrix[row]}, максимальное значение {my_max(matrix[row])}')
            matrix[row][matrix[row].index(my_max(matrix[row]))], matrix[row][0] = matrix[row][0], matrix[row][matrix[row].index(my_max(matrix[row]))]
            print(f'Полученный ряд {matrix[row]}\n')
        print(f'ПОлученная матрица:')
        for r in matrix:
            print("".join(f"{elem:8d}" for elem in r))
    
    def task11():
        import random
        
        matrix = [[random.randint(-10, 10) for _ in range(5)] for _ in range(7)]
        
        print('Первоначальная матрица:')
        for r in matrix: print("".join(f"{elem:8d}" for elem in r))
        
        cur_min_elem, cur_min_index = matrix[0][0], 0
        
        for i in range(7):
            if matrix[i][0] < cur_min_elem: 
                cur_min_elem = matrix[i][0]
                cur_min_index = i 
        
        print(f'Строка с наименьшим элементов в первом столбце это строка: {cur_min_index + 1}, сам элемент: {cur_min_elem}')
        
        matrix.pop(cur_min_index)
        
        print(f'Пoлученная матрица:')
        for r in matrix:
            print("".join(f"{elem:8d}" for elem in r))
    
    def task_17():
        
        def my_min(arr):
            cur_max = arr[0]
            for x in arr: cur_max = x if x < cur_max else cur_max
            return cur_max
    
        import random 
        
        n, m = int(input('Введите высоту матрицы: ')), int(input('Введите длину матрицы: '))
        
        matrix = [[random.randint(-10, 10) for _ in range(m)] for _ in range(n)]
        
        print('Первоначальная матрица:')
        for r in matrix: print("".join(f"{elem:8d}" for elem in r))
        
        for row in matrix:
            row.insert(0, row.pop(row.index(my_min(row))))
        print(f'Пoлученная матрица:')
        for r in matrix: print("".join(f"{elem:8d}" for elem in r))
    
class lvl3():
#4, 8 у лизы 
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

        magical_number = 10 ** (len(str(my_max(arr))) + 1)
        print('Первоначальный массив:', *arr)

        arr_o = [x / magical_number for x in arr]
        print('Преобразованный массив:', *arr_o)

        arr_u = [int(x * magical_number) for x in arr_o]
        print('Возвращённый массив:', *arr_u)

    def task14_dvumerniy():
        import random
        def my_max(arr):
            max_elem = float('-inf')
            for x in arr:
                if x > max_elem:
                    max_elem = x
            return max_elem
        
        def my_max_matrix(matrix):
            return my_max(my_max(map(abs, row)) for row in matrix)
        
        rows = int(input('Введите количество строк: '))
        cols = int(input('Введите количество столбцов: '))
        matrix = [[random.randint(-100, 100) for _ in range(cols)] for _ in range(rows)]

        magical_number = 10 ** (len(str(my_max_matrix(matrix))) + 1)
        print('Первоначальная матрица:')
        for r in matrix: print("".join(f"{elem:8}" for elem in r))

        matrix_o = [[x / magical_number for x in row] for row in matrix]
        print('Преобразованная матрица:')
        for r in matrix_o: print("".join(f"{elem:8}" for elem in r))

        matrix_u = [[int(x * magical_number) for x in row] for row in matrix_o]
        print('Возвращённая матрица:')
        for r in matrix_u: print("".join(f"{elem:8}" for elem in r))
