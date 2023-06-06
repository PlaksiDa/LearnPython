def open_contacts():
    try:
        with open('Sem_8\contacts.txt', 'r') as file:
            contacts = {}
            for line in file:
                name, number = line.strip().split(',')
                contacts[name] = number
            return contacts
    except FileNotFoundError:
        return {}

def save_contacts(contacts):
    with open('Sem_8\contacts.txt', 'w') as file:
        for name, number in contacts.items():
            file.write(f"{name},{number}\n")

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

def main():
    contacts = open_contacts()

    while True:
        print("Меню:")
        print("1. Показать все контакты")
        print("2. Добавить контакт")
        print("3. Найти контакт")
        print("4. Изменить контакт")
        print("5. Удалить контакт")
        print("6. Выйти")

        choice = input("Введите номер операции: ")

        if choice == "1":
            show_all_contacts(contacts)
        elif choice == "2":
            add_contact(contacts)
        elif choice == "3":
            find_contact(contacts)
        elif choice == "4":
            edit_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            save_contacts(contacts)
            break
        else:
            print("Некорректный выбор.")

if __name__ == "__main__":
    main()