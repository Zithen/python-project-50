import json


def generate_diff(file_path1, file_path2):
    file1_content = json.load(open(file_path1))
    file2_content = json.load(open(file_path2))
    keys_ = []

    for key in file1_content:
        keys_.append(key)

    keys_.sort()

    print(keys_)
