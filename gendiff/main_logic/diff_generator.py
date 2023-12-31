from gendiff.main_logic.file_parser import parse_files
from gendiff.main_logic.internal_view_creator import create_internal_view


def generate_diff(file_path1: str, file_path2: str) -> str:
    diff_container = {}
    file1_content, file2_content = parse_files(file_path1, file_path2)
    merged_files_content = dict(sorted((file1_content | file2_content).items()))
    print(create_internal_view(file1_content, file2_content))

    for key in merged_files_content:
        if key not in file2_content:
            diff_container['- ' + key] = merged_files_content[key]
        elif key not in file1_content:
            diff_container['+ ' + key] = merged_files_content[key]
        elif key in file1_content and merged_files_content[key] == file1_content[key]: # noqa E501
            diff_container['  ' + key] = merged_files_content[key]
        else:
            diff_container['- ' + key] = file1_content[key]
            diff_container['+ ' + key] = file2_content[key]

    diff_string = '{\n'
    for key, value in diff_container.items():
        diff_string += '  ' + key.replace("'", "") + ': ' + str(value).lower() + '\n' # noqa E501
    diff_string += '}'

    return diff_string
