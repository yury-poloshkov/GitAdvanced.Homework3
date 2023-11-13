from core.operations.impl.Find import Find
from ..Operation import Operation
from ...repository.db_connector import *

class Delete(Operation):
    operation = "delete"
    def execute(self, path):
        print("\033[H\033[J", end="")
        print("----- Удаление заметки -----")
        if input("Вам известен идентификатор заметки, которую вы хотите удалить (y/n): ").lower() == "n":
            operation = Find()
            operation.execute(path)
            print("----- Удаление заметки -----")
        note_index = input("Введите идентификатор удаляемой заметки: ")
        notes = read_all(path)
        successed = False
        for note in notes:
            if note.index == note_index:
                notes.remove(note)
                successed = True
        if successed == True:
            save_all(path, notes)
            print("Операция выполнена успешно: заметка с идентификатором %s удалена" %note_index)
        else:
            print("ERROR: Заметка с идентификатором %s не существует, либо была удалена ранее" %note_index)