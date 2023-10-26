import json


def generate_diff(file_path1, file_path2):
    file1_content = json.load(open(file_path1))
    file2_content = json.load(open(file_path2))
    diff = {}

    print(file1_content)
