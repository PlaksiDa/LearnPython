import contact_manager

MENU_CHOICES = {
    "1": contact_manager.show_all_contacts,
    "2": contact_manager.add_contact,
    "3": contact_manager.find_contact,
    "4": contact_manager.edit_contact,
    "5": contact_manager.delete_contact,
}

def print_menu():
    print("Меню:")
    print("1. Показать все контакты")
    print("2. Добавить контакт")
    print("3. Найти контакт")
    print("4. Изменить контакт")
    print("5. Удалить контакт")
    print("6. Выйти")

def handle_choice(choice, contacts):
    if choice in MENU_CHOICES:
        selected_function = MENU_CHOICES[choice]
        selected_function(contacts)
    else:
        print("Некорректный выбор.")