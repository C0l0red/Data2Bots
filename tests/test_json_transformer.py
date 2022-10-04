import json
import unittest

from element_type import ElementType
from exceptions import InvalidElementTypeError
from json_file_writer_reader import JsonFileWriterReader
from json_transformer import JsonTransformer

test_input_file_path = 'tests/text_files/test_input.json'
test_output_file_path = 'tests/text_files/test_output.json'


class MyTestCase(unittest.TestCase):
    def test_transform_returns_correct_data_shape(self):
        json_file_writer_reader = JsonFileWriterReader(test_input_file_path, test_output_file_path)
        json_transformer = JsonTransformer(json_file_writer_reader)

        data = {'name': 'John'}

        transformed_data = json_transformer.transform(data)

        self.assertEqual(list(transformed_data.get('name').keys()), ['type', 'tag', 'description', 'required'])

    def test_determine_type_detects_string(self):
        self.assertEqual(JsonTransformer.determine_type('name'), ElementType.STRING)

    def test_determine_type_detects_integer(self):
        self.assertEqual(JsonTransformer.determine_type(1), ElementType.INTEGER)

    def test_determine_type_detects_boolean(self):
        self.assertEqual(JsonTransformer.determine_type(True), ElementType.BOOLEAN)

    def test_determine_type_detects_enum(self):
        colors = ['RED', 'GREEN', 'BLUE']

        self.assertEqual(JsonTransformer.determine_type(colors), ElementType.ENUM)

    def test_determine_type_detects_array(self):
        people = [{'name': 'John'}, {'name': 'Jane'}]

        self.assertEqual(JsonTransformer.determine_type(people), ElementType.ARRAY)

    def test_determine_type_detects_object(self):
        person = {'name': 'John'}

        self.assertEqual(JsonTransformer.determine_type(person), ElementType.OBJECT)

    def test_determine_type_raises_exception_for_invalid_type(self):
        invalid_type = set()

        self.assertRaises(InvalidElementTypeError, JsonTransformer.determine_type, invalid_type)

    def test_run(self):
        expected_result = {
            'user': {
                'type': ElementType.OBJECT.name,
                'tag': '',
                'description': '',
                'required': False
            },
            'time': {
                'type': ElementType.INTEGER.name,
                'tag': '',
                'description': '',
                'required': False
            },
            'acl': {
                'type': ElementType.ARRAY.name,
                'tag': '',
                'description': '',
                'required': False
            },
            'publicFeed': {
                'type': ElementType.BOOLEAN.name,
                'tag': '',
                'description': '',
                'required': False
            },
            'internationalCountries': {
                'type': ElementType.ENUM.name,
                'tag': '',
                'description': '',
                'required': False
            },
            'topTraderFeed': {
                'type': ElementType.BOOLEAN.name,
                'tag': '',
                'description': '',
                'required': False
            },
        }

        json_file_writer_reader = JsonFileWriterReader(test_input_file_path, test_output_file_path)
        json_transformer = JsonTransformer(json_file_writer_reader)
        json_transformer.run()

        with open(test_output_file_path) as file:
            json_data = json.load(file)

        self.assertEqual(json_data, expected_result)



if __name__ == '__main__':
    unittest.main()
