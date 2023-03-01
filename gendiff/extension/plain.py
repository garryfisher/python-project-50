import json


def plain_format(diff, path=''):
    result = ''
    for item in diff:
        key = item['key']
        value = get_readability(item['value'])
        action = item['operation']
        if action == 'children':
            result += plain_format(value, path=path + f'{key}.') + '\n'
        elif action == 'added':
            result += f"Property '{path}{key}' was added with value: "
            result += f"{value}\n"
        elif action == 'deleted':
            result += f"Property '{path}{key}' was removed\n"
        elif action == 'updated':
            result += f"Property '{path}{key}' was updated. "
            result += f"From {value[0]} to {value[1]}\n"

        return result.strip()


def get_readability(raw_data):
    if isinstance(raw_data, dict):
        result = "[complex value]"
    elif isinstance(raw_data, tuple):
        result = get_readability(raw_data[0]), get_readability(raw_data[1])
    elif isinstance(raw_data, str):
        raw_data = json.dumps(raw_data).strip('"')
        result = f"'{raw_data}'"
    elif isinstance(raw_data, bool) or not raw_data:
        result = json.dumps(raw_data).strip('"')
    else:
        result = raw_data

    return result
