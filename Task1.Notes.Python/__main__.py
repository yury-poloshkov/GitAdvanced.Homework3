from core.repository.db_connector import create
from ui.note_view import show_menu

from core.operations.impl.Add import Add
from core.operations.impl.Change import Change
from core.operations.impl.Clear import Clear
from core.operations.impl.Delete import Delete
from core.operations.impl.List import List
from core.operations.impl.Find import Find
from core.operations.Operation import Operation


def init_functions(operations):
    operations.append(List())
    operations.append(Add())
    operations.append(Find())
    operations.append(Change())
    operations.append(Delete())
    operations.append(Clear())
    operations.append(Operation())

def main():
    print("\033[H\033[J", end="")
    try:
        path = input("Введите имя Вашей записной книжки: ")
        path = path + ".json"
        if path == ".json":
            path = "notes.json"
    except EOFError as e:
        path = "notes.json"
    create(path)
    operations = []
    init_functions(operations)
    show_menu(path, operations) 

if __name__ == "__main__":
    main()