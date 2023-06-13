# Задача №43
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.

import random

def gen_list(n):
    my_list = [random.randint(1, 10) for i in range(n)]
    return my_list


print(list_1 := gen_list(int(input("Введите количество элементов: "))))

def count_equal_pairs(numbers):
    count = 0
    unique_numbers = set(numbers)  # создаем множество из чисел списка, чтобы получить только уникальные значения

    for num in unique_numbers:
        num_count = numbers.count(num)  # считаем количество вхождений числа в список
        pairs = num_count // 2  # количество пар, образованных данным числом
        count += pairs

    return count

print(count_equal_pairs(list_1))

# print(sum([list_1.count(i)//2 for i in set(list_1)]))