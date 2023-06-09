import file_manager
import menu

def main():
    contacts = file_manager.open_contacts()

    while True:
        menu.print_menu()
        choice = input("Введите номер операции: ")

        if choice == "6":
            file_manager.save_contacts(contacts)
            break

        menu.handle_choice(choice, contacts)

if __name__ == "__main__":
    main()