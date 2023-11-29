def create_internal_view(file1_content, file2_content):
    diff = {}
    removed = file1_content.keys() - file2_content.keys()
    added = file2_content.keys() - file1_content.keys()
    unchanged = file1_content.keys() & file2_content.keys()

    for unchanged_key in unchanged:
        file1_value = file1_content[unchanged_key]
        file2_value = file2_content[unchanged_key]
        if isinstance(file1_value, dict) and isinstance(file2_value, dict):
            diff[unchanged_key] = {
                'state': 'nested',
                'value': create_internal_view(file1_value, file2_value),
            }
        elif file1_value == file2_value:
            diff[unchanged_key] = {
                'state': 'unchanged',
                'value': file1_content[unchanged_key],
            }
        else:
            diff[unchanged_key] = {
                'state': 'changed',
                'old_value': file1_value,
                'new_value': file2_value,
            }

    for removed_key in removed:
        diff[removed_key] = {
            'state': 'removed',
            'value': file1_value,
        }

    for added_key in added:
        diff[added_key] = {
            'state': 'added',
            'value': file2_value,
        }

    return diff
