import json
from deepdiff import DeepDiff
from dictdiffer import diff, patch


def generate_diff(file_path1, file_path2):
    with (open(file_path1) as file1, open(file_path2) as file2):
        file1_content = json.load(file1)
        file2_content = json.load(file2)
    
    file1_keys, file2_keys = [], []
    diff_container = '{\n'

    diff1 = patch(diff(file1_content, file2_content), file1_content)
    diff2 = patch(diff(file2_content, file1_content), file2_content)
    print(diff1)
    print(diff2)
