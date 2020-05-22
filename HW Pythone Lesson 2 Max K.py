# Задание № 1
my_list = [
    1, 2.05, True, 'Урал', [1, 2, 3],
    {1: 'Да'}, (1, 2, 3),
    {1, 2, 3, 4, 5}
]
for i in my_list:
    print(type(i))

# Задание № 2
my_list = []
while True:
    object_list = input('Введите любое число, слово, букву или символ: ')
    my_list.append(object_list)
    answer = input('Хотите ещё добавить число?(Y/N): ')
    if answer == 'Y':
        pass
    else:
        break
i = 0
k = 1
if len(my_list) % 2 == 0:
    while k <= len(my_list) - 1:
        my_list[i], my_list[k] = my_list[k], my_list[i]
        i += 2
        k += 2
else:
    while k <= len(my_list) - 2:
        my_list[i], my_list[k] = my_list[k], my_list[i]
        i += 2
        k += 2
print(my_list)

# Задание № 3 через словарь

month = int(input('Введите номер месяца: '))
month_dict = {
    1: 'Зимы',
    2: 'Зимы',
    3: 'Весны',
    4: 'Весны',
    5: 'Весны',
    6: 'Лета',
    7: 'Лета',
    8: 'Лета',
    9: 'Осени',
    10: 'Осени',
    11: 'Осени',
    12: 'Зимы'
}
print('{} это месяц {}'.format(month, month_dict[month]))

# Задание № 3 через список

month = int(input('Введите номер месяца: '))
month_list = [
    'Нулевой индекс', 'Зимы', 'Зимы',
    'Весны', 'Весны', 'Весны', 'Лета',
    'Лета', 'Лета', 'Осени', 'Осени',
    'Осени', 'Зимы'
]
print('{} это месяц {}'.format(month, month_list[month]))

# Задание № 4

phrases = input('Введите фразу из нескольких слов: ').split(' ')
for phrase in phrases:
    if len(phrase) > 10:
        phrases_fix = phrase[:10]
for i in range(len(phrases)):
    if len(phrases[i]) > 10:
        phrases[i] = phrases_fix
    print(i + 1, phrases[i])

# Задание № 5

rating_list = [15, 15, 12, 12, 10, 8, 5, 5, 3, 3, 2]
print(rating_list)
rating_number = int(input('Введите новый элемент рейтинга (любое число): '))
for i in range(len(rating_list)):
    if rating_list[-1] == rating_number:
        rating_list.append(rating_number)
        break
    elif rating_list[i] == rating_number and rating_list[i + 1] < rating_number:
        rating_list.insert(i, rating_number)
        break
    elif rating_list[i] < rating_number and rating_list.count(rating_number) == 0:
        rating_list.insert(i, rating_number)
    elif rating_list[i] > rating_number and rating_list.count(rating_number) == 0:
        rating_list.append(rating_number)
print(rating_list)
