# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.

import random

n = int(input("Введите общее количество монеток: "))

i = 0
count_head = 0
count_tail = 0
coin_list = []

for i in range(n):
    coin_list.append(random.randint(0, 1))
    if coin_list[i] == 0:
        count_head += 1
    else:
        count_tail += 1

print(coin_list)

if count_head > count_tail:
    print(f"Нужно перевернуть {count_tail} монет с решкой")
else:
    print(f"Нужно перевернуть {count_head} монет с орлом")
