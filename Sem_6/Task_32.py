# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)

import random


def gen_list(n):
    my_list1 = [random.randint(1, 10) for i in range(n)]
    return my_list1


print(list_1 := gen_list(int(input("Введите количество элементов: "))))

min_num = int(input("Введите минимальный диапазон: "))
max_num = int(input("Введите максимальный диапазон: "))

list_2 = []
for i in list_1:
    if min_num < i < max_num:
        list_2.append(i)

print(list_2)
