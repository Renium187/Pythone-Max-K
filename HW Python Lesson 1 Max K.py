# Задание № 1

def div1(divident, divider):
    try:
        divident = float(input("Укажите делимое: "))
        divider = float(input("Укажите делитель: "))
        quotient = divident / divider
    except ValueError:
        print('Введите целые или дробные числа')
        return
    except ZeroDivisionError:
        print('Деление на ноль!')
        return
    quotient = divident / divider
    return print('Частное', quotient)
div1(1, 1)

# Задание № 2

def biogaph(**kwargs):
    return kwargs
print(biogaph(Имя = 'Max', Фамилия = 'Rezanov',
              Год_рождения = 1987, Город_проживания =
              'Химки', E_mail = 'ggg@maail.ru', телефон =
              678910).values())

# Задание № 3

def my_func(number_1, number_2, number_3):
    list_my_fync = sorted([number_1, number_2, number_3], reverse = True)
    sum = list_my_fync[0] + list_my_fync[1]
    return sum
print(my_func(1, 7, 23))

# Задание № 4 через **

def my_funk(x, y):
    expression = x ** y
    return expression
print(my_funk(5, -3))

# Задание № 4 через цикл

def my_funk(x, y):
    i = 1
    if y < 0:
        x = 1 / x
    expression = x
    while i < abs(y):
        if y == 0:
            expression = 1
            break
        expression *= x
        i += 1
    return round(expression, 4)
print(my_funk(5, -3))

# Задание № 5

sum_list = 0
i = None
while i != 'Q':
    my_list = input('Введите несколько чисел через пробел для суммирования, Q выход: ').split()
    if my_list.count('Q') != 0:
        q_index = my_list.index('Q')
        my_list = my_list[:q_index]
        i = 'Q'
    my_list_int = map(lambda number: int(number), my_list)
    sum_list += sum(my_list_int)
    print(sum_list)

# Задание № 6

def int_func(word):
    return word.title()
print(int_func('макентош'))
my_strs = input('Введите несколько слов с маленькой буквы: ').split()
my_strs_title = []
for my_str in my_strs:
    my_str_title = int_func(my_str)
    my_strs_title.append(my_str_title)
print(' '.join(my_strs_title))