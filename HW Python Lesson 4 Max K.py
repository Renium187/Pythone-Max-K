# Задача № 1
from sys import argv


def salary(hours, per_hour, bonus):
    cash = int(hours) * int(per_hour) + int(bonus)
    return cash


print(salary(argv[1], argv[2], argv[3]))

# Задача № 2

number = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
bl = [number[i] for i in range(1, len(number)) if number[i] > number[i - 1]]
print(bl)

bonus_task_list = [n for n in range(20, 241) if n % 20 == 0 or n % 21 == 0]
print(bonus_task_list)

# Задача № 3

numbers = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
count_numbers = [number for number in numbers if numbers.count(number) == 1]
print(count_numbers)

# Задача № 4
from functools import reduce

prod_list = [n for n in range(100, 1001)]
product = reduce(lambda x, y: x * y, prod_list)
print(product)

# Задача № 5
from itertools import count, cycle

for i in count(3):
    if i > 10:
        break
    else:
        print(i)

my_list = [n for n in range(1, 6)]
turns = 0
for m in cycle(my_list):
    if turns > 20:
        break
    else:
        print(m)
    turns += 1

# Задача № 6
from math import factorial


def fact(n):
    for i in range(1, n + 1):
        prod = factorial(i)
        yield prod


for el in fact(10):
    print(el)

