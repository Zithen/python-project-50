def create_internal_view(file1_content, file2_content):
    diff = {}
    removed = file1_content.keys() - file2_content.keys()
    added = file2_content.keys() - file1_content.keys()
    unchanged = file1_content.keys() & file2_content.keys()

    for key in unchanged:
        file1_value = file1_content[key]
        file2_value = file2_content[key]
        if isinstance(file1_value, dict) and isinstance(file2_value, dict):
            diff[key] = {
                'state': 'nested',
                'value': create_internal_view(file1_value, file2_value), }
        elif file1_value == file2_value:
            diff[key] = {
                'state': 'unchanged',
                'value': file1_content[key],
            }
        else:
            diff[key] = {
                'state': 'changed',
                'old_value': file1_value,
                'new_value': file2_value,
            }

    for key in removed:
        diff[key] = {
            'state': 'removed',
            'value': file1_value,
        }

    for key in added:
        diff[key] = {
            'state': 'added',
            'value': file2_value,
        }

    return diff
