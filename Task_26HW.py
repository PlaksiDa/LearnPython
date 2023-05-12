# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.

def power(a, b):
    if b == 0:
        return 1
    elif b % 2 == 0:
        return power(a, b // 2) ** 2
    else:
        return a * power(a, b - 1)
        
a = int(input("Введите число: "))
b = int(input("Введите степень: "))

print(f"Число {a} в степени {b} = {power(a, b)}")