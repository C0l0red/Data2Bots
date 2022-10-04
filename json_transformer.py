from element_type import ElementType
from exceptions import InvalidElementTypeError
from json_file_writer_reader import JsonFileWriterReader


class JsonTransformer:
    json_file_writer_reader: JsonFileWriterReader

    def __init__(self, json_file_writer_reader: JsonFileWriterReader):
        self.json_file_writer_reader = json_file_writer_reader

    def transform(self, json_data: dict) -> dict:
        transformed_json: dict = {}

        for key in json_data.keys():
            value = {
                'type': self.determine_type(json_data.get(key)).name,
                'tag': '',
                'description': '',
                'required': False
            }

            transformed_json.update({key: value})

        return transformed_json

    @staticmethod
    def determine_type(element) -> ElementType:
        if isinstance(element, str):
            return ElementType.STRING
        elif isinstance(element, bool):
            return ElementType.BOOLEAN
        elif isinstance(element, int):
            return ElementType.INTEGER
        elif isinstance(element, list):
            if len(element) > 0 and isinstance(element[0], str):
                return ElementType.ENUM
            else:
                return ElementType.ARRAY
        elif isinstance(element, dict):
            return ElementType.OBJECT
        else:
            raise InvalidElementTypeError(f'Unsupported data type {element}')

    def run(self):
        json_data = self.json_file_writer_reader.read_from_file()
        json_data = json_data.get('message')

        transformed_json_data: dict = self.transform(json_data)

        self.json_file_writer_reader.write_to_file(transformed_json_data)

