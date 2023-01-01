# 3 Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу 
# между максимальным и минимальным значением дробной части элементов.

import random

my_list = []
for i in range(0,10):
    my_list.append(random.randrange(0, 1000)/100)
print(my_list)

# Выделяем дробную часть в отдельный список
part_list = []
for  num in my_list:
    part_list.append(round(num - int(str(num).split('.')[0]), 3))
print(part_list)

# Ищем мин и максимальное значение
min_num = max_num = part_list[0]
for i in range(len(part_list)-1):
    # max_num = part_list[i]
    if part_list[i] > max_num:
       max_num = part_list[i] 
    if part_list[i] < min_num:
       min_num = part_list[i]
difference = (max_num - min_num)
print(f'Difference betwin min and max fractional part equals {difference}')
