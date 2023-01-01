# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов 
# списка, стоящих на нечётной позиции.

import random

my_list = []
for i in range(0,10):
    my_list.append(random.randrange(0,100))
print(my_list)
sum = 0
for i in my_list[1:10:2]:
    sum+=i
print(f'Сумма нечетных элементов равна {sum}')
