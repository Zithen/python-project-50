from gendiff import generate_diff

FILE_PATH1 = '/home/zithen/education/hexlet_python_projects/python-project-50/gendiff/files/file1.json'
FILE_PATH2 = '/home/zithen/education/hexlet_python_projects/python-project-50/gendiff/files/file2.json'

diff = generate_diff(FILE_PATH1, FILE_PATH2)
print(diff)
