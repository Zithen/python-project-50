import re
import yaml
import json


def parse_files(file_path1, file_path2):
    with (open(file_path1) as file1, open(file_path2) as file2):
        if re.match('^.*(.json)$', file_path1) and re.match('^.*(.json)$', file_path2): # noqa E501
            file1_content, file2_content = json.load(file1), json.load(file2)
        elif re.match('^.*(.yml|.yaml)$', file_path1) and re.match('^.*(.yml|.yaml)$', file_path2): # noqa E501
            file1_content, file2_content = yaml.load(file1, Loader=yaml.Loader), yaml.load(file2, Loader=yaml.Loader) # noqa E501
        else:
            return 'Unknown format'

    return (file1_content, file2_content)
