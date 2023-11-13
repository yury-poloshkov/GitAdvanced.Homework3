from core.repository.JSONmapper import JSONmapper

def create(path):
    try:
        file = open(path, 'r')
    except IOError:
        file = open(path, 'w')
        print('Создана новая записная книжка \> ' + path)
    finally:
        file.close()

def read_all(path):
    file = open(path, 'r')
    records = list()
    for line in file:
        records.append(JSONmapper.from_json(line))
    file.close()
    return records

def save_all(path, records):
    file = open(path, 'w')
    file.writelines("%s\n" % JSONmapper.to_json(record) for record in records)
    file.close()

def save_record(path, new_record):
    file = open(path, 'a')
    file.write(JSONmapper.to_json(new_record) + "\n")
    file.close()    