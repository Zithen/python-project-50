import yaml
import json


JSON = '.json'
YML = '.yml'
YAML = '.yaml'


def parse_files(file_path1, file_path2): # noqa C901
    with (open(file_path1) as file1, open(file_path2) as file2):
        if JSON in file_path1:
            file1_content = json.load(file1)
        elif YML in file_path1 or YAML in file_path1:
            file1_content = yaml.load(file1, Loader=yaml.Loader)
        if JSON in file_path2:
            file2_content = json.load(file2)
        elif YML in file_path2 or YAML in file_path2:
            file2_content = yaml.load(file2, Loader=yaml.Loader)

    try:
        return (file1_content, file2_content)
    except UnboundLocalError:
        raise RuntimeError('Unsupported file format')
