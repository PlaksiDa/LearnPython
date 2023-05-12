# Задача №27. Решение в группах
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
import string

text = input("Введите текст: ")

for ch in string.punctuation: # или for ch in ".,!"
    text = text.replace(ch,"")

words = text.lower().split()  # Разбиваем текст на слова, используя пробелы как разделитель
unique_words = set(words)  # Преобразуем список слов в множество уникальных слов
num_unique_words = len(unique_words)  # Вычисляем количество уникальных слов

print(f"Количество уникальных слов: {num_unique_words}")