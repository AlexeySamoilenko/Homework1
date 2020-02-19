import json
from xml.dom import minidom
from abc import ABC, abstractmethod


class FileHandler():
    def __init__(self):
        pass

    @staticmethod
    def reading_file(file_path: str) -> tuple:
        with open(file_path, 'r', encoding='utf-8') as f:
            return tuple(json.load(f))

    @staticmethod
    def data_processing(room_file_path: str, students_file_path: str) -> dict:
        data_from_file = FileHandler.reading_file(room_file_path)
        dict_for_merge = {}
        for i in data_from_file:
            dict_for_merge[i['id']] = ['Room #' + str(i['id'])]

        data_from_file = FileHandler.reading_file(file_path2)
        for i in data_from_file:
            dict_for_merge[i['room']].append(i['name'])

        result_data = {}
        for value in dict_for_merge.values():
            result_data[value[0]] = value[1:]
        return result_data


class FileSaver(ABC):
    def __init__(self, result_data: dict, save_path_file: str):
        self.result_data = result_data
        self.save_path_file = save_path_file

    @abstractmethod
    def save_data(self, result_data: dict, save_path_file: str):
        pass


class XmlSaver(FileSaver):
    def __init__(self, result_data: dict, save_path_file: str):
        super(XmlSaver, self).__init__(result_data, save_path_file)

    def save_data(self):
        # Save file in XML format
        root = minidom.Document()
        xml = root.createElement('root')
        root.appendChild(xml)

        for key, value in self.result_data.items():
            roomChild = root.createElement('room')
            roomChild.appendChild(root.createTextNode(key + ':' + str(value)))
            xml.appendChild(roomChild)
        xml_str = root.toprettyxml(indent='\t')

        with open(self.save_path_file, 'w') as f:
            f.write(xml_str)


class JsonSaver(FileSaver):
    def __init__(self, result_data: dict, save_path_file: str):
        super(JsonSaver, self).__init__(result_data, save_path_file)

    def save_data(self):
        #Save data in Json format
        with open(self.save_path_file, "w") as f:
            json.dump(self.result_data, f)


def main(file_path: str, file_path2: str, save_path_file: str):
    result_data = FileHandler.data_processing(file_path, file_path2)
    
    if '.json' in save_path_file:
        JsonSaver(result_data, save_path_file).save_data()
    elif '.xml' in save_path_file:
        XmlSaver(result_data, save_path_file).save_data()
    else:
        return False


if __name__ == "__main__":
    main('rooms.json', 'students.json', 'result.json')
    main('rooms.json', 'students.json', 'result.xml')
    



  
