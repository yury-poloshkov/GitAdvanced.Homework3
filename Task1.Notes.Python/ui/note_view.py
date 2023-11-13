def show_menu(path, operations):
    user_choice = "none"
    while user_choice != "exit":
        print("\033[H\033[J", end="")
        print("----- Записная книжка v.2023.07.28 -----")
        print("Connected NoteBook: " + path + "\n")
        print("----- ГЛАВНОЕ МЕНЮ -----")
        for operation in operations:
            print("  " + operation.operation.upper())
        user_choice = input("\Введите команду> ")
        user_choice = user_choice.lower()
        for operation in operations:
            if operation.operation == user_choice:
                operation.execute(path)
                if operation.operation != "exit":
                    timeout()

def timeout():
    input("\nPress ENTER to continue...\n")