import json


def get_json(diff):
    return json.dumps(get_dict(diff), indent=2)


def get_dict(diff_lst):
    result = {}
    for item in diff_lst:
        key = item['key']
        value = item['value']
        operation = item['operation']
        if isinstance(value, list):
            result.setdefault(key, {
                'operation': operation,
                'value': get_dict(value)})
        elif isinstance(value, tuple):
            result.setdefault(key, {
                'operation': operation,
                'value': {
                    'old': value[0],
                    'new': value[1]}})
        else:
            result.setdefault(key, {
                'operation': operation,
                'value': value})

    return result
