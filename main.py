from json_file_writer_reader import JsonFileWriterReader
from json_transformer import JsonTransformer

input_file_path = 'tests/text_files/test_input.json'
output_file_path = 'tests/text_files/test_output.json'

if __name__ == '__main__':
    print('Creating JsonFileWriterReader instance...')
    json_file_writer_reader = JsonFileWriterReader(input_file_path, output_file_path)

    print('Creating JsonTransformer instance...')
    json_transformer = JsonTransformer(json_file_writer_reader)

    print('Running transformation...')
    json_transformer.run()

    print('Done', end='\n')
    print('Check in tests/text_files/test_output.json for results')

