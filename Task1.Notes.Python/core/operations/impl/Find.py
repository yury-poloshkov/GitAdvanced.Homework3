import re

from core.repository.Note import *
from ..Operation import Operation
from ...repository.db_connector import *

class Find(Operation):
    operation = "find"

    def execute(self, path):
        print("\033[H\033[J", end="")
        print("----- Поиск заметок в записной книжке %s -----" %path)
        search_mask = input("Введите маску поиска: ")
        if ((len(search_mask) == 10) & (re.match(r'[\d]{2}.[\d]{2}.[\d]{4}',search_mask) != '')):
            search_mask = search_mask[-4:]+ "-" + search_mask[-7:-5] + "-" + search_mask[:2]
        if ((len(search_mask) == 7) & (re.match(r'[\d]{2}.[\d]{4}',search_mask) != '')):
            search_mask = search_mask[-4:]+ "-" + search_mask[:2]
        if ((len(search_mask) == 5) & (re.match(r'[\d]{2}.[\d]{2}',search_mask) != '')):
            search_mask = search_mask[-2:]+ "-" + search_mask[:2]
        notes = read_all(path)
        found_notes = list()
        for note in notes:
            if (re.search(search_mask, str(note)) != None):
                found_notes.append(note)
        print("----- Результаты поиска -----")
        if len(found_notes) != 0:
            found_notes.sort(key=Note.get_date, reverse = True)
            for note in found_notes:
                print(note)
        else: 
            print("Заметок, соответсвующих критерию поиска, не обнаружено")