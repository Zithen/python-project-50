import json


def generate_diff(file_path1, file_path2):
    file1_content = json.load(open(file_path1))
    file2_content = json.load(open(file_path2))
    file1_keys, file2_keys = [], []
    diff_container = {}


    for key in file1_content:
        file1_keys.append(key)
    for key in file2_content:
        file2_keys.append(key)

    file1_keys.sort()

    for key in file1_keys:
        if key not in file2_keys:
            key_new = '- ' + key
            diff_container[key_new] = file1_content[key]
        
        elif file1_content[key] == file2_content[key]:
            diff_container[key] = file1_content[key]
        
        elif file1_content[key] != file2_content[key]:
            key_new = '+ ' + key
            diff_container[key_new] = file2_content[key]

    print(json.dumps(diff_container, indent = 4))
