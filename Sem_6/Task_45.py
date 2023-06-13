# Задача №45
# Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящее 105. Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает).

k = int(input())

sum_1 = 0
sum_2 = 0
list_result = []
my_set = set()
my_list = []


def dividers_sum(k):
    my_list = []
    for i in range(1, k):
        if k % i == 0:
            my_list.append(i)
    return sum(my_list)


for i in range(1, k + 1):
    sum_1 = dividers_sum(i)
    sum_2 = dividers_sum(dividers_sum(i))
    if i == sum_2 and sum_1 != sum_2:
        my_list.append(sum_1)

for i in range(0, len(my_list) - 1, 2):
    print(my_list[i], my_list[i + 1])
