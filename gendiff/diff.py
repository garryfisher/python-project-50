def get_diff(file1, file2):
    all_keys = sorted(set(file1.keys()) | set(file2.keys()))
    diff_lst = []
    for key in all_keys:
        cur_value1 = file1.get(key, 'key_no_found')
        cur_value2 = file2.get(key, 'key_no_found')
        if isinstance(cur_value1, dict) and isinstance(cur_value2, dict):
            diff_lst.append(get_element(
                key, get_diff(cur_value1, cur_value2), 'children')
            )
        elif cur_value1 == cur_value2:
            diff_lst.append(get_element(key, cur_value1, 'no_changed'))
        elif cur_value2 == 'key_no_found':
            diff_lst.append(get_element(key, cur_value1, 'deleted'))
        elif cur_value1 == 'key_no_found':
            diff_lst.append(get_element(key, cur_value2, 'added'))
        else:
            diff_lst.append(
                get_element(key, (cur_value1, cur_value2), 'updated')
            )

    return diff_lst


def get_element(key, value, operation):
    return {
        "key": key,
        "value": value,
        'operation': operation
    }
