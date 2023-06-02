# Задача №41. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.

import random


def gen_list(n):
    my_list = [random.randint(1, 10) for i in range(n)]
    return my_list


print(list_1 := gen_list(int(input("Введите количество элементов: "))))

count = 0

for i in range(1, len(list_1) - 1):
    if list_1[i - 1] < list_1[i] > list_1[i + 1]:
        count += 1

print(count)

print(len([i for i in range(1, len(list_1) - 1) if list_1[i - 1] < list_1[i] > list_1[i + 1]])) # list compilation