from gendiff import generate_diff

FILE_PATH1 = '/home/zithen/education/hexlet_python_projects/python-project-50/gendiff/files/file1.json' # noqa E501
FILE_PATH2 = '/home/zithen/education/hexlet_python_projects/python-project-50/gendiff/files/file2.json' # noqa E501

diff = generate_diff(FILE_PATH1, FILE_PATH2)
print(diff)

