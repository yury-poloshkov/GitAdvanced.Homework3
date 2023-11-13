from core.repository.Note import Note
from ..Operation import Operation
from ...repository.db_connector import *

from datetime import date

class Add(Operation):

    operation = "new"

    def execute(self, path):
        print("\033[H\033[J", end="")
        print("----- Создание новой заметки -----")
        note_topic = input("Введите тему: ")
        while len(note_topic) == 0:
            note_topic = input("Тема заметки не может быть пустой, повторите ввод: ")
        note_body = input("Введите содержание: ")
        index = str(1)
        notes = read_all(path)
        if len(notes) != 0:
            last_note = (notes.pop())
            index = str(int(last_note.index)+1)
        note = Note(index, str(date.today()), note_topic, note_body)
        try:
            save_record(path, note)
            print("Информация успешно сохранена в %s" %path)
        except IOError:
            print("ERROR: ошибка сохранения данных")