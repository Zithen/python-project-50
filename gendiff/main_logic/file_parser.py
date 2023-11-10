import yaml
import json


EXTENSIONS_OPERATIONS = {
    'json': json.load,
    'yml': yaml.safe_load,
    'yaml': yaml.safe_load,
}


def parse_files(file_path1, file_path2):
    file1_extension = file_path1.split('.')[-1]
    file2_extension = file_path2.split('.')[-1]

    if file1_extension not in EXTENSIONS_OPERATIONS.keys() or file2_extension not in EXTENSIONS_OPERATIONS.keys(): # noqa E501
        raise RuntimeError(f'Unsupported file format, supported formats are {", ".join(EXTENSIONS_OPERATIONS.keys())}') # noqa E501

    with (open(file_path1) as file1, open(file_path2) as file2):
        file1_content = EXTENSIONS_OPERATIONS[file1_extension](file1)
        file2_content = EXTENSIONS_OPERATIONS[file2_extension](file2)

    return (file1_content, file2_content)
