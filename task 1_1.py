from xml.dom import minidom
import json


def reading_file(file_path: str):
    with open(file_path, 'r', encoding='utf-8') as f:
        return tuple(json.load(f))

def filfuling_file(data, result_path):
    with open(result_path, "w") as f:
        json.dump(data, f)

def data_processing(file_path: str,file_path2: str) -> dict:
    file_text = reading_file(file_path)
    d = {}
    for i in file_text:
        d[i['id']] = ['Room #' + str(i['id'])]

    file2_text = reading_file(file_path2)
    for i in file2_text:
        d[ i['room'] ].append( i['name'] )

    result_dict = {}
    for value in d.values():
        result_dict[value[0]] = value[1:]
    return result_dict
        
def createXML(result_dict: dict):
    root = minidom.Document()
    xml = root.createElement('root')
    root.appendChild(xml)
    
    for key, value in result_dict.items():
        roomChild = root.createElement('room')
        roomChild.appendChild(root.createTextNode(key))
        xml.appendChild(roomChild)
    
        childOfRoom = root.createElement('list of people')
        childOfRoom.appendChild(root.createTextNode(str(value)))
        roomChild.appendChild(childOfRoom)
    
    xml_str = root.toprettyxml(indent='\t')
    save_path_file = 'result.xml'

    with open(save_path_file, 'w') as f:
        f.write(xml_str)

def main(file_path: str, file_path2: str, output_format: str):

    result_data = data_processing(file_path, file_path2)

    if output_format == 'json':    
        filfuling_file(result_data, 'result.json')
    elif output_format == 'xml':
        createXML(result_data)
    else:
        return False


if __name__ == "__main__":

    main('rooms.json', 'students.json', 'json')
    main('rooms.json', 'students.json', 'xml')
  
