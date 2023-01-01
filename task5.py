# 5 Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных 
# индексов.

fib_list = [0, 1]
neg_fib_list = [1,-1]


num = int(input('Enter number of members fibonacci series: '))
for memb in range(2, num):
    fib_list.append(fib_list[memb - 1] + fib_list[memb - 2])
    neg_fib_list.append(neg_fib_list[memb - 2] - neg_fib_list[memb - 1])

final_list = neg_fib_list[:-1]
final_list.reverse()
final_list.extend(fib_list)
print(final_list)
