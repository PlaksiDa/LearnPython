# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии:
# an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

first_num = int(input("Введите первое число: "))
step = int(input("Введите шаг: "))
n = int(input("Введите количество элементов: "))

print(my_list := [i for i in range(first_num, n + 1, step)])
