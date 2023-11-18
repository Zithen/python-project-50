'''def walk_through_children(key, file_content):
    if isinstance(key, dict):
        return
'''


def create_internal_view(file1_content, file2_content):
    added = file2_content.keys() - file1_content.keys()
    removed = file1_content.keys() - file2_content.keys()
    unchanged = file1_content.keys() & file2_content.keys()

    print(f'added: {added}')
    print('\n')
    print(removed)
    print('\n')
    print(unchanged)
    print('\n')
