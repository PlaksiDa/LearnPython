def show_all_contacts(contacts):
    if not contacts:
        print("Телефонный справочник пуст.")
    else:
        print("Все контакты:")
        for name, number in contacts.items():
            print(f"Имя: {name}, Телефон: {number}")

def add_contact(contacts):
    name = input("Введите имя контакта: ")
    number = input("Введите номер телефона контакта: ")
    contacts[name] = number
    print("Контакт добавлен.")

def find_contact(contacts):
    name = input("Введите имя контакта для поиска: ")
    if name in contacts:
        print(f"Имя: {name}, Телефон: {contacts[name]}")
    else:
        print("Контакт не найден.")

def edit_contact(contacts):
    name = input("Введите имя контакта для редактирования: ")
    if name in contacts:
        new_number = input("Введите новый номер телефона: ")
        contacts[name] = new_number
        print("Контакт изменен.")
    else:
        print("Контакт не найден.")

def delete_contact(contacts):
    name = input("Введите имя контакта для удаления: ")
    if name in contacts:
        del contacts[name]
        print("Контакт удален.")
    else:
        print("Контакт не найден.")