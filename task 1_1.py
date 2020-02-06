import json, re
from collections import defaultdict 

def reading_file(file_path: str):
    with open(file_path, 'r', encoding='utf-8') as f:
        return tuple(json.load(f))

def filfuling_file():
    text1 = reading_file('rooms.json')
    text2 = reading_file('students.json')
    return text1, text2

def filfuling_file():
    data = 1
    with open("result.json", "w") as f:
        json.dump(data, write_file)

    

def regular_way():
    room_number = 123123
    reg = r"Room #{0}\b,".format(room_number)
    d[reg].append('имя фамилия')


def crd():
    text1 = reading_file('rooms.json')
    d = defaultdict(lambda: None)
    for i in text1:
        d[i['id']] = { i['name']:[] }
    d=dict(d)
    d=[d]
    text2 = reading_file('students.json')

    with open("result.json", "w") as f:
        json.dump(d, f)
crd()


