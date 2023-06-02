# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
# в порядке

def count_vowels(word):
    vowels = 'аеёиоуыэюя'
    count = 0
    for char in word:
        if char.lower() in vowels:
            count += 1
    return count

def check_vowel_counts(sentence):
    words = sentence.split()
    vowel_counts = [count_vowels(word) for word in words]

    if len(set(vowel_counts)) == 1:
        print("Парам пам-пам")
    else:
        print("Пам парам")

sentence = input("Введите предложение: ")
check_vowel_counts(sentence)