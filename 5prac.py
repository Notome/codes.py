import matplotlib.pyplot as plt

def my_len(arrstring):
    return my_sum(1 for _ in arrstring)

def my_sum(arr):
    result = 0 
    for x in arr:
        result += x 
    return result 

def my_strip(string):
    i = 0
    while i < my_len(string) and not (string[i] in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'): i += 1
    if i == my_len(string): return ''
    string, j = string[i:], 1
    while j <= my_len(string) and not (string[-j] in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'): j += 1
    string = string[:-j+1]
    return string

def my_split(string, splitter=' '):
    result = []
    current_result = ''
    for char in string:
        if char == splitter:
            if current_result:
                my_append(result, current_result)
                current_result = ''
        else:
            current_result += char
    if current_result:
        my_append(result, current_result)
    return result

def my_readline(file):
    return [x for x in file]

def linear_interpolation(x, y, num_points=1000000):
    x_new, y_new = [], []
    
    for i in range(my_len(x) - 1):
        x0, x1, y0, y1 = x[i], x[i + 1], y[i], y[i + 1]
        for j in range(num_points // (my_len(x) - 1)):
            x_interp, y_interp = x0 + (x1 - x0) * (j / (num_points // (my_len(x) - 1))), y0 + (y1 - y0) * (j / (num_points // (my_len(x) - 1)))
            my_append(x_new, x_interp)
            my_append(y_new, y_interp)
    return x_new, y_new

def my_map(func, lst):
    return [func(x) for x in lst]

def my_append(lst, item):
    lst[len(lst):] = [item]

def my_max(arr):
    cur_max = float('-inf')
    for x in arr: cur_max = cur_max if x < cur_max else x 
    return cur_max

def my_min(arr):
    cur_max = float('inf')
    for x in arr: cur_max = cur_max if x > cur_max else x 
    return cur_max

def approximation(xs, ys):
    n, degree = len(xs), 4
    
    A = [[my_sum(xi ** (i + j) for xi in xs) for j in range(degree + 1)] for i in range(degree + 1)]
    B = [my_sum(ys[i] * (xs[i] ** j) for i in range(n)) for j in range(degree + 1)]
    
    for i in range(degree + 1):
        for j in range(i + 1, degree + 1):
            if A[i][i] == 0: raise ValueError("Матрица вырождена")
            ratio = A[j][i] / A[i][i]
            for k in range(i, degree + 1): A[j][k] -= ratio * A[i][k]
            B[j] -= ratio * B[i]

    coeffs = [0] * (degree + 1)
    for i in range(degree, -1, -1): coeffs[i] = (B[i] - sum(A[i][j] * coeffs[j] for j in range(i + 1, degree + 1))) / A[i][i]

    x_fit = [my_min(xs) + i * (my_max(xs) - my_min(xs)) / 100 for i in range(101)]
    y_fit = [my_sum(coeffs[j] * xi ** j for j in range(degree + 1)) for xi in x_fit]

    return x_fit, y_fit

def my_replace(string, replacable, replacement):
    new_string = ''
    i = 0
    while i < len(string):
        if string[i:i + len(replacable)] == replacable:
            new_string += replacement
            i += len(replacable)  #
        else:
            new_string += string[i]
            i += 1  
    return new_string

def task1():
    with open('C:\\Users\\n3455\\.vscode\\2711\\1lvl.txt', 'r') as file:
        lines = [my_map(int, my_split(x[:my_len(x) - 1], '\t')) for x in my_readline(file)]
        xs, ys = lines[0], lines[1]
        x_new, y_new = linear_interpolation(xs, ys)
    plt.figure(figsize=(10, 6))
    plt.plot(xs, ys, 'o', label='Исходные данные', color='red')
    plt.plot(x_new, y_new, '-', label='Интерполированные данные', color='blue')
    plt.title('Интерполяция данных')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.grid()
    plt.show()
#task1()

def task2():
    with open('C:\\Users\\n3455\\.vscode\\2711\\2lvl.txt', 'r') as file:
        lines = [(my_split(x[:my_len(x) - 1], '\t')) for x in my_readline(file)]
        xs, ys = my_map(float ,[my_replace(x, ',', '.') for x in lines[0]]), my_map(float ,[my_replace(x, ',', '.') for x in lines[1]])
        x_fit, y_fit = (approximation(xs, ys))
    plt.scatter(xs, ys, label='Исходные данные', color='red')
    plt.plot(x_fit, y_fit, label='Линейная аппроксимация', color='blue')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Апроксимация функции методом наименьших квадратов')
    plt.legend()
    plt.show()
#task2()
