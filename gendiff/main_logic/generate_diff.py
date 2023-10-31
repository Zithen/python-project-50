import json
from deepdiff import DeepDiff
from dictdiffer import diff, patch


def generate_diff(file_path1, file_path2):
    with (open(file_path1, 'r') as file1, open(file_path2, 'r') as file2):
        file1_content = json.load(file1)
        file2_content = json.load(file2)
    
    file1_keys, file2_keys = [], []
    diff_container = '{\n'

    diff1 = diff(file1_content, file2_content)
    diff2 = diff(file2_content, file1_content)
    print(patch(diff1, file1_content))
    print(patch(diff2, file2_content))
