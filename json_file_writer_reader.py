import json

from exceptions import InvalidJsonError


class JsonFileWriterReader:
    input_file_path: str
    output_file_path: str

    def __init__(self, input_file_path, output_file_path):
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path

    def read_from_file(self) -> dict:
        with open(self.input_file_path) as file:
            try:
                json_data: dict = json.load(file)
            except json.decoder.JSONDecodeError as e:
                raise InvalidJsonError('Input file does not contain valid JSON')

        return json_data

    def write_to_file(self, data):
        try:
            json_data = json.dumps(data, indent=4)
        except TypeError:
            raise InvalidJsonError('Attempting to parse invalid JSON')

        with open(self.output_file_path, 'w') as file:
            file.write(json_data)

        return
