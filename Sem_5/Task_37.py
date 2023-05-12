# Задача №37
# Дано натуральное число N и
# последовательность из Т элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).

import random

def reverse_print(lst):
    if not lst:  
        return
    reverse_print(lst[1:])  
    print(lst[0])  
    
my_list = [random.randint(1, 100) for _ in range(10)]

print(my_list)
reverse_print(my_list)