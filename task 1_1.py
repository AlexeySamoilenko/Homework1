﻿import json
from xml.dom import minidom


def reading_file(file_path: str) -> tuple:
    with open(file_path, 'r', encoding='utf-8') as f:
        return tuple(json.load(f))

def filfuling_file(result_data: dict, save_path_file: str):
    with open(save_path_file, "w") as f:
        json.dump(result_data, f)

def data_processing(file_path: str, file_path2: str) -> dict:
    file_text = reading_file(file_path)
    dict_for_merge = {}
    for i in file_text:
        dict_for_merge[i['id']] = ['Room #' + str(i['id'])]

    file2_text = reading_file(file_path2)
    for i in file2_text:
        dict_for_merge[ i['room'] ].append( i['name'] )

    result_data = {}
    for value in dict_for_merge.values():
        result_data[value[0]] = value[1:]
    return result_data
        
def create_xml(result_data: dict, save_path_file: str):
    root = minidom.Document()
    xml = root.createElement('root')
    root.appendChild(xml)
    
    for key, value in result_data.items():
        roomChild = root.createElement('room')
        roomChild.appendChild(root.createTextNode(key+':'+str(value)))
        xml.appendChild(roomChild)
    xml_str = root.toprettyxml(indent='\t')

    with open(save_path_file, 'w') as f:
        f.write(xml_str)


def main(file_path: str, file_path2: str, save_path_file: str):

    result_data = data_processing(file_path, file_path2)

    if '.json' in save_path_file:    
        filfuling_file(result_data, save_path_file)
    elif '.xml' in save_path_file:
        create_xml(result_data, save_path_file)
    else:
        return False


if __name__ == "__main__":
    main('rooms.json', 'students.json', 'result.json')
    main('rooms.json', 'students.json', 'result.xml')
    



  
