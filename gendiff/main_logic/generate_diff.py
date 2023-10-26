import json


def generate_diff(file_path1, file_path2):
    print(json.load(open(file_path1)))