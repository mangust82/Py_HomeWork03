# 2 Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем 
# первый и последний элемент, второй и предпоследний и т.д.

import random

N = int(input('Введите размерность списка: '))
my_list = []
for i in range(0,N):
    my_list.append(random.randrange(0,10))
print(my_list)

list_result = []
for i in range(round(len(my_list) / 2)):
    list_result.append(int(my_list[i]) * int(my_list[-i-1]))
print(list_result)