def create_internal_view(file1_content, file2_content):
    print('\n')
    print(file1_content)
    print('\n')
    print(file2_content)
    print('\n')
    added = file2_content.keys() - file1_content.keys()
    removed = file1_content.keys() - file2_content.keys()
    common = file1_content.keys() & file2_content.keys()

    for elem in added:
        depth = 1
        if not isinstance(elem, dict):
            return file2_content.get(elem)
    print(added)
    print('\n')
    print(removed)
    print('\n')
    print(common)
    print('\n')
