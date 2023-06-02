# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
# столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
# почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
# ровно два аргумента, как, например, у операции умножения.


def print_operation_table(operation, num_rows=6, num_columns=6):
    # Печать заголовка
    print("   ", end="")
    for col in range(1, num_columns + 1):
        print(f"{col:4}", end="")
    print()

    # Печать разделительной строки
    print("----" * num_columns)

    # Печать содержимого таблицы
    for row in range(1, num_rows + 1):
        print(f"{row:2} |", end="")
        for col in range(1, num_columns + 1):
            result = operation(row, col)
            print(f"{result:4}", end="")
        print()

print_operation_table(lambda x, y: x + y, num_rows=10, num_columns=10)
