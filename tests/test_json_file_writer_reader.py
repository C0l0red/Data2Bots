import unittest
import json

from exceptions import InvalidJsonError
from json_file_writer_reader import JsonFileWriterReader

test_input_file_path = 'tests/text_files/test_input.json'
test_output_file_path = 'tests/text_files/test_output.json'


class MyTestCase(unittest.TestCase):
    def test_read_from_file(self):
        json_file_writer_reader = JsonFileWriterReader(test_input_file_path, test_output_file_path)
        json_data = json_file_writer_reader.read_from_file()

        self.assertIsInstance(json_data, dict)
        self.assertEqual(json_data.get('attributes').get('sensitive'), False)

    def test_read_from_file_raises_for_invalid_json(self):
        invalid_json_path = 'tests/text_files/invalid_input.json'

        json_file_writer_reader = JsonFileWriterReader(invalid_json_path, test_output_file_path)

        self.assertRaises(InvalidJsonError, json_file_writer_reader.read_from_file)

    def test_write_to_file(self):
        data = {'key': 'value'}
        json_data = json.dumps(data, indent=4)

        json_file_writer_reader = JsonFileWriterReader(test_input_file_path, test_output_file_path)
        json_file_writer_reader.write_to_file(data)

        with open(test_output_file_path) as file:
            self.assertEqual(file.read(), str(json_data))

    def test_write_to_file_raises_for_invalid_json(self):
        invalid_data = {"jane", "doe"}

        json_file_writer_reader = JsonFileWriterReader(test_input_file_path, test_output_file_path)

        self.assertRaises(InvalidJsonError, json_file_writer_reader.write_to_file, invalid_data)

    def doCleanups(self) -> None:
        with open(test_output_file_path, 'w') as file:
            file.truncate(0)


if __name__ == '__main__':
    unittest.main()
