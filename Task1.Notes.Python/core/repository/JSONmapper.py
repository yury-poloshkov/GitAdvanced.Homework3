import json
from core.repository.Note import Note

class JSONmapper:
    @staticmethod
    def to_json(note):
        if isinstance(note, Note):
            return json.dumps({
                "index": note.index,
                "date": note.date,
                "title": note.title,
                "body": note.body,
                })
    @staticmethod
    def from_json(record):
        record = json.loads(record)
        try:
            return Note(record["index"], 
                        record["date"], 
                        record["title"], 
                        record["body"])
        except AttributeError:
            print("Неверная структура")