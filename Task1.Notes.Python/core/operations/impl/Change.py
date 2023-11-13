from datetime import date
from core.operations.impl.Find import Find
from ..Operation import Operation
from ...repository.db_connector import *


class Change(Operation):
    operation = "edit"
    def execute(self, path):
        print("\033[H\033[J", end="")
        print("----- Редактирование заметки -----")
        if input("Вам известен идентификатор заметки, которую вы хотите отредактировать (y/n): ").lower() == "n":
            operation = Find()
            operation.execute(path)
            print("\n----- Редактирование заметки -----")
        note_index = input("Введите идентификатор редактируемой заметки: ")
        notes = read_all(path)
        successed = False
        for note in notes:
            if note.index == note_index:
                print("\n--- нажмите ENTER для пропуска корректировки поля ---")
                note_topic = input("\nВведите новую тему: ")
                if len(note_topic) != 0:
                    note.title = note_topic
                    note.date = str(date.today())
                    successed = True
                note_body = input("\nВведите новое содержание: ")
                if len(note_body) != 0:
                    note.body = note_body
                    note.date = str(date.today())
                    successed = True
        if successed == True:
            save_all(path, notes)
            print("\nОперация выполнена успешно: заметка с идентификатором %s перезаписана" %note_index)
        else:
            print("\nERROR: Заметка с идентификатором %s не существует, либо не была скорректирована" %note_index)