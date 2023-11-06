from gendiff.main_logic.gener_diff import generate_diff


FILE_PATH1 = '/home/zithen/education/hexlet_python_projects/python-project-50/gendiff/files/file1.json' # noqa E501
FILE_PATH2 = '/home/zithen/education/hexlet_python_projects/python-project-50/gendiff/files/file2.json' # noqa E501

def test_basic():
    assert generate_diff(FILE_PATH1, FILE_PATH2) == '{\n  - follow: false\n    host: hexlet.io\n  - proxy: 123.234.53.22\n  - timeout: 50\n  + timeout: 20\n  + verbose: true\n}'
