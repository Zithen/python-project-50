result = {}


def merge_files(file1_c, file2_c):
    merged_files_content = dict(sorted((file1_c | file2_c).items()))
    return merged_files_content


def find_added(file1_content, file2_content):
    added = file2_content.keys() - file1_content.keys()
    for item in added:
        return file2_content.get(item)


def find_removed(file1_content, file2_content):
    return file1_content.keys() - file2_content.keys()


def find_unchanged(file1_content, file2_content):
    return file1_content.keys() & file2_content.keys()


def walk(tree, depth=1):
    for key, elem in tree.items():
        if isinstance(elem, dict):
            result.update({key: {'state': 'nested', 'depth': depth, 'value': elem}})
            walk(elem, depth + 1)
        else:
            result.update({key: {'state': 'value', 'depth': depth, 'value': elem}})
    
    return result


def create_internal_view(file1_content, file2_content):
    return merge_files(file1_content, file2_content)
