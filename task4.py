# 4 Напишите программу, которая будет преобразовывать десятичное число в двоичное.

from os import system

system("cls")

a = int(input('Enter a number to convert to binary: '))
print(a)
print(bin(a))

bin_list = []
rest = 0
res = a
while res != 0:
    rest = res % 2
    res = res // 2
    bin_list.append(str(rest))
bin_list.reverse()   
print('  ' +''.join(bin_list))
