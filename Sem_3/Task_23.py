# Задача №23
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)

import random

my_list = [random.randint(1, 100) for _ in range(10)]
print(my_list)
count = 0

for i in range(1, len(my_list)):
    if my_list[i] > my_list[i - 1]:
        count += 1

print(count)
