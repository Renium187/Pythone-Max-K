# # Задача № 1
#
# simple_list = []
# keyboard = True
# while keyboard != False:
#     simple_str = input('Введите слово:')
#     if simple_str:
#         simple_list.append(simple_str)
#     else:
#         keyboard = False
# with open('my_log.txt', 'w', encoding='utf-8') as f:
#     for n in simple_list:
#         f.write(n + '\n')

## Задача № 2

# with open('My_text', 'r') as f:
#     list_numbers = []
#     for num, value in enumerate(f, 1):
#         list_numbers.append(num)
#         list_words = value.split()
#         list_n_words = []
#         for num_w, words in enumerate(list_words, 1):
#             list_n_words.append(num_w)
#         print(f'Количество слов в {num} строке - {list_n_words[-1]}')
#     print('Число строк -', list_numbers[-1])

# # Задача № 3
#
# with open('Salary', 'r') as f:
#     doc_list = [value.split() for value in f]
#     n_list = [doc_list[i][0] for i in range(len(doc_list))]
#     sal_list = [int(doc_list[i][1]) for i in range(len(doc_list))]
#     for n in range(len(sal_list)):
#         if sal_list[n] >= 20000:
#             print(f'{n_list[n]} получает больше 20000, а именно {sal_list[n]}')
#     aver_sal = sum(sal_list) / len(sal_list)
#     print(f'Средняя зарплата = {aver_sal}')

# # Задание № 4
#
# doc_dict = {
#     'One': 'Один',
#     'Two': 'Два',
#     'Three': 'Три',
#     'Four': 'Четыре',
# }
# with open('Numbers', 'r') as f:
#     ll = [lines.split('-') for lines in f]
#     for i in range(len(ll)):
#         ll[i][0] = doc_dict[ll[i][0]]
#         ll[i] = '-'.join(ll[i])
#     print(ll)
# with open('Номера', 'w', encoding='utf-8') as g:
#     for m in ll:
#         g.write(m)

# # Задание №5
#
# num_list = [n for n in range(1, 11)]
# with open('Числа.txt', 'w', encoding='utf-8') as f:
#      for i in num_list:
#          f.write(f'{i} ')
# with open('Числа.txt', 'r') as g:
#     ln = [lines.split() for lines in g]
#     int_ln = [int(i) for i in ln[0]]
#     sum_g = sum(int_ln)
#     print(sum_g)

# # Задание № 6
#
# with open('Studies', 'r') as f:
#     list_st = [lines.split(':') for lines in f]
#     key_list = []
#     value_list = []
#     for i in range(len(list_st)):
#         key_list.append(list_st[i][0])
#         cor_i = list_st[i][1].replace('(', ' ')
#         inner_l = cor_i.split()
#         inner_sum_l = []
#         for n in inner_l:
#             if n.isdigit():
#                 n = int(n)
#                 inner_sum_l.append(n)
#         inner_sum = sum(inner_sum_l)
#         value_list.append(inner_sum)
#     print(dict(zip(key_list, value_list)))

# Задание № 7
import json

profit_list = []
result = []
list_firms = []
with open('Finance', 'r') as f:
    list_fin = [lines.split() for lines in f]
    for i in range(len(list_fin)):
        list_firms.append(list_fin[i][0])
        profit = int(list_fin[i][2]) - int(list_fin[i][3])
        print(f'Прибыль {list_fin[i][0]} = {profit}')
        profit_list.append(profit)
    for n in profit_list:
        if n < 0:
            n = 0
    aver_pr = sum(profit_list) / len(profit_list)
    print(f'Средняя прибыль по предприятиям: {aver_pr}')
    fin_dict = dict(zip(list_firms, profit_list))
    result.append(fin_dict)
    aver_fin_dict = {'Средняя прибыль': aver_pr}
    result.append(aver_fin_dict)
    #print(result)
with open('tracks.json', 'w', encoding='utf-8') as g:
    json.dump(result, g)
    print('Преобразование завершено')

