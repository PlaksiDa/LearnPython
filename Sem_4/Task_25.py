# Задача №25
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.

string = input("Введите строку: ")
characters = {}  # Словарь для хранения количества повторений каждого символа

for char in string:
    if char in characters:
        # Если символ уже встречался ранее, увеличиваем его счетчик на 1
        characters[char] += 1
        # Добавляем к символу постфикс с номером повторения
        new_char = char + "_" + str(characters[char])
    else:
        # Если символ встречается в первый раз, добавляем его в словарь с счетчиком 1
        characters[char] = 1
        # Новый символ не требует постфикса
        new_char = char
    print(new_char, end=" ")  # Выводим новый символ с постфиксом или без

print()  # Переходим на новую строку