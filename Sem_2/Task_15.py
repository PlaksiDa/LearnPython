# Задача №15.
# Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза

import random
import sys

n = int(input("Введите количество арбузов: "))

watermelon_min = 15
watermelon_max = 3
watermelon_weights_list = []
# watermelon_weights = [random.randint(3, 15) for i in range(n)]

for i in range(n):
    watermelon_weights_list.append(random.randint(3, 15))
    if watermelon_weights_list[i] < watermelon_min:
        watermelon_min = watermelon_weights_list[i]
    if watermelon_weights_list[i] > watermelon_max:
        watermelon_max = watermelon_weights_list[i]

print(watermelon_weights_list)
print(f"Самый лёгкий арбуз, весом {watermelon_min}, располагается на позиции {watermelon_weights_list.index(watermelon_min)+1}")
print(f"Самый тяжелый арбуз, весом {watermelon_max}, располагается на позиции {watermelon_weights_list.index(watermelon_max)+1}")
