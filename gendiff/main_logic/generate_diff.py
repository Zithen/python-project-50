import json


def generate_diff(file_path1, file_path2):
    with (open(file_path1) as file1, open(file_path2) as file2):
        file1_content = json.load(file1)
        file2_content = json.load(file2)
    diff_container = {}
    merged_files_content = dict(sorted(({**file1_content, **file2_content}).items()))

    for key in merged_files_content:
        if key not in file2_content:
            diff_container['- ' + key] = merged_files_content[key]
        elif key not in file1_content:
            diff_container['+ ' + key] = merged_files_content[key]
        elif key in file1_content and merged_files_content[key] == file1_content[key]:
            diff_container['  ' + key] = merged_files_content[key]
        else:
            diff_container['- ' + key] = file1_content[key]
            diff_container['+ ' + key] = file2_content[key]

    diff_string = '{\n'
    for key, value in diff_container.items():
        diff_string += '  ' + key.replace("'", "") + ': ' + str(value).lower() + '\n'
    diff_string += '}'

    return diff_string
