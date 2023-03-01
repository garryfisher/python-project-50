import json


def json_format(diff):
    return json.dumps(get_dict(diff), indent=2)


def get_dict(diff):
    result = {}
    for item in diff:
        key = item['key']
        value = item['value']
        action = item['operation']
        if isinstance(value, list):
            result.setdefault(key, {
                'action': action,
                'value': get_dict(value)})
        elif isinstance(value, tuple):
            result.setdefault(key, {
                'action': action,
                'value': {
                    'old': value[0],
                    'new': value[1]}})
        else:
            result.setdefault(key, {
                'action': action,
                'value': value})

        return result
