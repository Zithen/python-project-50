import yaml
import json


EXTENSIONS = {
    'json': 'json.load',
    'yml': 'yaml.safe_load',
    'yaml': 'yaml.safe_load',
} # noqa E123
JSON, YML, YAML = EXTENSIONS
JSON_LOAD = '.load'
YAML_LOAD = '.safe_load'


def file_to_dict(file_path, file_extension):
    pass


def parse_files(file_path1, file_path2):
    file1_extension = file_path1.split('.')[-1]
    file2_extension = file_path2.split('.')[-1]

    if file1_extension not in EXTENSIONS.keys() or file2_extension not in EXTENSIONS.keys():
        raise RuntimeError(f'Unsupported file format, supported formats are {", ".join(EXTENSIONS.keys())}') # noqa E501

    with (open(file_path1) as file1, open(file_path2) as file2):
        if JSON in file_path1:
            file1_content = json.load(file1)
        elif YML in file_path1 or YAML in file_path1:
            file1_content = yaml.safe_load(file1)
        if JSON in file_path2:
            file2_content = json.load(file2)
        elif YML in file_path2 or YAML in file_path2:
            file2_content = yaml.safe_load(file2)

    return (file1_content, file2_content)
