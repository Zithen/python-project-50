import json
from deepdiff import DeepDiff
from dictdiffer import diff, patch


def generate_diff(file_path1, file_path2):
    file1_content = json.load(open(file_path1))
    file2_content = json.load(open(file_path2))
    file1_keys, file2_keys = [], []
    diff_container = '{\n'


    for key in file1_content:
        file1_keys.append(key)
    for key in file2_content:
        file2_keys.append(key)

    file1_keys.sort()

    for key in file1_keys:
        if key not in file2_keys:
            diff_key = '  - ' + key + ': ' + str(file1_content[key]) + ',' + '\n'
            diff_container += diff_key           
        
        elif file1_content[key] == file2_content[key]:
            pass
        
        elif file1_content[key] != file2_content[key]:
            pass

    diff1 = diff(file1_content, file2_content)
    diff2 = diff(file2_content, file1_content)
    print(patch(diff1, file1_content))
    print(patch(diff2, file2_content))
