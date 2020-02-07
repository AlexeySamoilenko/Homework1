import json


def reading_file(file_path: str):
    with open(file_path, 'r', encoding='utf-8') as f:
        return tuple(json.load(f))

def filfuling_file(data, result_path):
    with open(result_path, "w") as f:
        json.dump(data, f)

def crd():
    text1 = reading_file('rooms.json')
    d = {}
    for i in text1:
        d[i['id']] = ['Room #' + str(i['id'])]

    text2 = reading_file('students.json')
    for i in text2:
        d[ i['room'] ].append( i['name'] )

    result_dict = {}
    for value in d.values():
        result_dict[value[0]] = value[1:]
        
    filfuling_file(result_dict, 'result.json')

    
crd()


