import math

#1. Определить средний рост девочек и мальчиков одного класса. В 
#классе учится n учеников. 
def task_1_1():
    boys_height, girls_height = [], []

    def average(arr):
        return sum(arr) / len(arr) if arr else 0  

    try:
        n = int(input("Введите пожалуйста число детей в классе: "))
    except ValueError:
        print("Некорректный ввод. Попробуйте еще раз.")
        return

    for i in range(n):
        gender = input(f"Введите пол для ребенка {i + 1} (м - мальчик, ж - девочка): ").strip().lower()

        if gender not in ['м', 'ж']:
            print("Некорректный ввод. Пожалуйста, введите 'м' для мальчика или 'ж' для девочки.")
            continue  

        height = input('Введите рост (число): ')

        try:
            height = int(height)
            if gender == 'м':
                boys_height.append(height)
            elif gender == 'ж':
                girls_height.append(height)
        except ValueError:
            print("Пожалуйста, введите корректный рост в числовом формате.")
            continue  

    print(f'Рост мальчиков: {boys_height}\nРост девочек: {girls_height}')
    print(f'Средний рост мальчиков: {average(boys_height)}\nСредний рост девочек: {average(girls_height)}')
#task_1_1()

def task_1_2():
    boys_height, girls_height = [], []
    
    def average(arr):
        return sum(arr) / len(arr) if arr else 0  

    current_gender = None

    while True:
        gender = input("Введите пол (м - мальчик, ж - девочка, q - выход): ").strip().lower()
        
        if gender == 'q': break 
        
        if gender in ['м', 'ж']: 
            current_gender = gender  

            while True:
                height = input('Введите рост (или "с" для смены пола): ')
                
                if height == 'с':
                    break  
                try:
                    height = int(height)
                    if current_gender == 'м':
                        boys_height.append(height)
                    elif current_gender == 'ж':
                        girls_height.append(height)
                except ValueError:
                    print("Пожалуйста, введите корректный рост в числовом формате.")

        else:
            print("Некорректный ввод. Пожалуйста, используйте 'м' для мальчика, 'ж' для девочки, или 'q' для выхода.")

    print(f'Рост мальчиков: {boys_height}\nРост девочек: {girls_height}')
    print(f'Средний рост мальчиков: {average(boys_height)}\nСредний рост девочек: {average(girls_height)}')
#task_1_2()


#6. В компьютер по очереди вводятся координаты n точек. Определить, 
#сколько из них принадлежит фигуре, ограниченной осью абсцисс и 
#аркой синусоиды, построенной для аргумента от 0 до pi.   

def task_6_1():
    n = int(input("Введите количество точек: "))
    points = []

    def count_points_in_area(points):
        count = 0
        for x, y in points:
            if 0 <= x <= math.pi and 0 <= y <= math.sin(x):
                count += 1
        return count

    for _ in range(n):
        try:
            x, y = map(float, input("Введите координаты точки (x y): ").split())
            points.append((x, y))
            result = count_points_in_area([points[-1]])  # Проверяем только текущую точку
            if result > 0:
                print(f'Так как x = {x}, что больше 0 и меньше {math.pi}, а y = {y}, что больше 0 и меньше sin(x) = {math.sin(x)}. То ({int(x)},{int(y)}) принадлежит графику.')
            else:
                if not(0 <= x <= math.pi):
                    print(f'Так как x = {x}, что не больше 0 или меньше {math.pi}. То ({int(x)}, {int(y)}) не принадлежит графику.')
                else:
                    print(f'Так как y = {y}, что меньше 0 или больше sin(x) = {math.sin(x)}. То ({int(x)}, {int(y)}) не принадлежат графику.')
        except ValueError:
            print('Были введены неправильные значения.')

    total_count = count_points_in_area(points)
    print("Общее количество точек, принадлежащих графику:", total_count)
#task_6_1()

def task_6_2():
    def count_points_in_area(points):
        count = 0
        for x, y in points:
            if 0 <= x <= math.pi and 0 <= y <= math.sin(x):
                count += 1
        return count

    points = []

    while True:
        user_input = input("Введите координаты точки (x y) или 'стоп' для завершения: ")
        if user_input.lower() == 'стоп':
            break
        try:
            x, y = map(float, user_input.split())
            points.append((x, y))
            result = count_points_in_area([points[-1]])  
            if result > 0:
                print(f'Так как x = {x}, что больше 0 и меньше {math.pi}, а y = {y}, что больше 0 и меньше sin(x) = {math.sin(x)}. То ({(x)},{(y)}) принадлежит графику.')

            else:
                if not(0 <= x <= math.pi):
                    print(f'Так как x = {x}, что не больше 0 или меньше {math.pi}. То ({(x)}, {(y)}) не принадлежит графику.')
                else:
                    print(f'Так как y = {y}, что меньше 0 или больше sin(x) = {math.sin(x)}. То ({(x)}, {(y)}) не принадлежат графику.')
    
        except ValueError:
            print('Были введены неправильные значения.')

    total_count = count_points_in_area(points)  # Подсчет всех точек после ввода
    print("Общее количество точек, принадлежащих графику:", total_count)
#task_6_2()

#13.  Для n пар значений А, В вычислить по выбору площадь 
#прямоугольника со сторонами А, В; площадь кольца, заключенного 
#между двумя окружностями с радиусами А и В; площадь 
#равнобедренного треугольника со сторонами А, B, В. 

def task_13_1():
    n = int(input("Введите количество пар: "))
    lst = []
    
    for _ in range(n):
        while True:
            try:
                x, y = map(float, input("Введите пару значений, x y: ").split())
                lst.append([x, y])
                
                inp = int(input('Если вам нужно вычислить площадь прямоугольника, введите: 1\nЕсли вам нужно вычислить площадь кольца между двумя окружностями, введите: 2\nЕсли вам нужно вычислить площадь равнобедренного треугольника, введите: 3\n'))
                
                if inp not in [1, 2, 3]:
                    print('Выберите из предложенных вариантов.')
                    continue
                break 
                
            except ValueError:
                print('Были введены неправильные значения. Попробуйте снова.')

        current_pair = lst[-1]  

        
        if inp == 1: 
            print('Выбрана площадь прямоугольника')
            area_rectangle = current_pair[0] * current_pair[1]
            print(f'Площадь прямоугольника со сторонами A= {current_pair[0]}, B= {current_pair[1]}, равна {area_rectangle}')
        
        elif inp == 2:  
            if current_pair[0] > current_pair[1]:
                area_ring = math.pi * (current_pair[0] ** 2 - current_pair[1] ** 2)
                print('Выбрана площадь кольца между двумя окружностями')
                print(f'Площадь кольца, при окружностях A= {current_pair[0]}, B= {current_pair[1]}, равна {area_ring}')
            else:
                print('Ошибка: Радиус внешней окружности должен быть больше радиуса внутренней.')
        
        elif inp == 3:
            print('Выбрана площадь равнобедренного треугольника')
            a = current_pair[0]  
            b = current_pair[1]  
            if b > (a / 2):
                height = math.sqrt(b ** 2 - (a / 2) ** 2)
                area_triangle = (a * height) / 2
                print(f'Площадь равнобедренного треугольника со сторонами A= {a}, B= {b}, равна {area_triangle}')
            else:
                print('Ошибка: Длина равных сторон должна быть больше половины основания.')
#task_13_1()

def task_13_2():
    while True:
        command = input("Введите 'стоп' для выхода или любую клавишу для продолжения: ")
        if command.lower() == "стоп":
            print("Выход из программы.")
            break

        try:
            x, y = map(float, input("Введите пару значений, x y: ").split())
        except ValueError:
            print('Были введены неправильные значения. Попробуйте снова.')
            continue  

        while True:
            try:
                inp = int(input('Если вам нужно вычислить площадь прямоугольника, введите: 1\nЕсли вам нужно вычислить площадь кольца между двумя окружностями, введите: 2\nЕсли вам нужно вычислить площадь равнобедренного треугольника, введите: 3\nПоле ввода: '))
                
                if inp not in [1, 2, 3]:
                    print('Выберите из предложенных вариантов.')
                    continue
                
                break 
                
            except ValueError:
                print('Выберите из предложенных вариантов.')
        
        if inp == 1: 
            print('Выбрана площадь прямоугольника')
            area_rectangle = x * y
            print(f'Площадь прямоугольника со сторонами A= {x}, B= {y}, равна {area_rectangle}\n')
        
        elif inp == 2: 
            if x > y:
                area_ring = math.pi * (x ** 2 - y ** 2)
                print('Выбрана площадь кольца между двумя окружностями')
                print(f'Площадь кольца, при окружностях A= {x}, B= {y}, равна {area_ring}\n')
            else:
                print('Ошибка: Радиус внешней окружности должен быть больше радиуса внутренней.')
        
        elif inp == 3: 
            print('Выбрана площадь равнобедренного треугольника')
            a = x  
            b = y  
            if b > (a / 2):
                height = math.sqrt(b ** 2 - (a / 2) ** 2)
                area_triangle = (a * height) / 2
                print(f'Площадь равнобедренного треугольника со сторонами A= {a}, B= {b}, равна {area_triangle}\n')
            else:
                print('Ошибка: Длина равных сторон должна быть больше половины основания.')
#task_13_2()
