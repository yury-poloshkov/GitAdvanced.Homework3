from ..Operation import Operation
from ...repository.db_connector import *

class Clear(Operation):
    operation = "clear"
    def execute(self, path):
        print("\033[H\033[J", end="")
        print("----- Очистка записной книжки %s -----" %path)
        confirmation = input("Вы действительно хотите удалить все записи из записной книжки %s (y/n): " %path).lower()
        if confirmation == "y":
            no_notes = list()
            save_all(path, no_notes)
            print("Записная книжка %s очищена" %path)
        else: print("Операция очистки записной книжки %s отменена" %path)