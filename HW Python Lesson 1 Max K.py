# Задание № 1

a = 24
b = 10
c = 4
print(a, b, c)

list_numb = []
list_str = []
i = 1
n = 1
while i < 4:
    number = int(input('Введите число № {}: '.format(i)))
    list_numb.append(number)
    i += 1
print(list_numb)

while n < 4:
    str = input('Введите существительное № %s: ' % (n))
    list_str.append(str)
    n += 1
print(list_str)

# Задание № 2

sec = int(input('Введите значение времени в секундах: '))
hour = 0
minute = 0
if sec > 3600:
    hour = sec // 3600
    minute = (sec - hour * 3600) // 60
    sec_view = sec - hour * 3600 - minute * 60
elif sec < 3600 and sec > 60:
    minute = sec // 60
    sec_view = sec - minute * 60
else:
    sec_view = sec
print('%s : %s : %s' % (hour, minute, sec_view))

# Задание № 3

n = input('Введите число n: ')
sum = int(n) + int(n * 2) + int(n * 3)
print('Cумма n+nn+nnn = ', sum)

# Задание № 4

a = int(input('Введите целое положительное число: '))
m = a % 10
a = a // 10
while a > 0:
    if a % 10 > m:
        m = a % 10
    a = a // 10
print(m)

# Задание № 5

income = int(input('Введите значение выручки компании: '))
spend = int(input('Введите значение издержек компании: '))
if income > spend:
    print('Прибыль')
    rent_index = income / spend * 100
    print('Рентабельность равна ', round(rent_index, 2), '%')
elif income < spend:
    print('Убыток')
else:
    print('Выходите на ноль')
pers = int(input('Какова численность сотрудников компании: '))
pers_income = income / pers
print('Прибыль компании из расчёта на 1 сотрудника: ', round(pers_income, 2))

# Задание 6

first_day = 2
last_day = 8
iter = 1
while first_day <= last_day:
    first_day = 1.1 * first_day
    iter += 1
print('Ответ: на {} день спортсмен достиг результата \
    - не менее {} км'.format(iter, last_day))

# Направляю на проверку