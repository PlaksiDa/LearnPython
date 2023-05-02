# Задача №11
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.

# n = int(input("Введите предел для числа фибоначи: "))
# search_num = int(input("Введите искомое число: "))

# fib_list = [0, 1]

# while len(fib_list) < n:
#     fib_list.append(fib_list[-1] + fib_list[-2])

# print(fib_list)

# if search_num in fib_list:
#     print(fib_list.index(search_num) + 1)
# else:
#     print("Такого числа нет в списке")

search_num = int(input("Введите искомое число: "))

first = 0
second = 1
index = 1

while second < search_num:
    first, second = second, first + second
    index += 1
print(index + 1 if second == search_num else -1)
