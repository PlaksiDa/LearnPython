# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.

a = int(input("Укажите сумму двух чисел: "))
b = int(input("Укажите произведение двух чисел: "))

for i in range(a):
    for j in range(b):
        if a == i + j and b == i * j:
            print(f"Это числа {i} и {j}")
