# Задача №19.
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

k = int(input("Введите k: "))
my_list = [1, 2, 3, 4, 5, 6]

seq = my_list[-k:] + my_list[:-k]
print(seq)
