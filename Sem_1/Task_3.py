# Задача №3
# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.

class1 = int(input("Количество учеников в 1 классе: "))
class2 = int(input("Количество учеников во 2 классе: "))
class3 = int(input("Количество учеников в 3 классе: "))
sum_students = class1 + class2 + class3
sum_desks = (sum_students // 2) + (sum_students % 2)
print(f"Необходимо купить {sum_desks} парт")