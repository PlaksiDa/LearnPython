# Задача №1.
# За день машина проезжает n километров. Сколько
# дней нужно, чтобы проехать маршрут длиной m
# километров? При решении этой задачи нельзя
# пользоваться условной инструкцией if и циклами.

n = int(input("Введите расстояние, которое проезжает машина за 1 день "))
m = int(input("Введите расстояние, которое нужно проехать "))
day = (m + n - 1) // n
print(f"Для того, чтобы проехать {m} км, машине понадобится {day} дней")