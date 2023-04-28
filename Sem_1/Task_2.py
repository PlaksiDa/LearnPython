# Задача 2: 
# Найдите сумму цифр трехзначного числа.

num = int(input("Введите трехзначное число: "))
digit1 = num // 100
digit2 = (num // 10) % 10
digit3 = num % 10
sum_of_digits = digit1 + digit2 + digit3
print("Сумма цифр трехзначного числа равна", sum_of_digits)