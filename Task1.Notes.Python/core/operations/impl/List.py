from core.repository.Note import *
from ..Operation import Operation
from ...repository.db_connector import *

class List(Operation):
    operation = "list"
    def execute(self, path):
        print("\033[H\033[J", end="")
        print("----- Список заметок  -----")
        notes = read_all(path)
        if len(notes) != 0:
            notes.sort(key=Note.get_date, reverse = True)
            for note in notes:
                print(note)
        else: print("Заметок в записной книжке %s не обнаружено" %path)        