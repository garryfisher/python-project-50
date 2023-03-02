def get_diff(file1, file2):
    all_keys = sorted(set(file1.keys()) | set(file2.keys()))
    diff = []
    for key in all_keys:
        value1 = file1.get(key, '!none')
        value2 = file2.get(key, '!none')
        if isinstance(value1, dict) and isinstance(value2, dict):
            diff.append(
                get_element(key, get_diff(value1, value2), 'children')
            )
        elif value1 == value2:
            diff.append(get_element(key, value1, 'no_changed'))
        elif value2 == '!none':
            diff.append(get_element(key, value1, 'deleted'))
        elif value1 == '!none':
            diff.append(get_element(key, value2, 'added'))
        else:
            diff.append(
                get_element(key, (value1, value2), 'updated')
            )

    return diff


def get_element(key, value, operation):
    return {
        "key": key,
        "value": value,
        "operation": operation
    }
