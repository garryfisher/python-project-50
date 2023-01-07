OPEN_BRACKET = '{'
CLOSE_BRACKET = '}'
SPACE = '    '
ADD = '  + '
DEL = '  - '
END = '\n'


"""
{'key': 'follow', 'value': 'key_no_found', 'operation': 'added'}
{'key': 'host', 'value': 'hexlet.io', 'operation': 'no_changed'}
{'key': 'proxy', 'value': 'key_no_found', 'operation': 'added'}
{'key': 'timeout', 'value': ('50', '20'), 'operation': 'update'}
{'key': 'verbose', 'value': 'key_no_found', 'operation': 'deleted'}
"""


def get_converting(dict_):
    key = dict_['key']
    value = dict_['value']
    action = dict_['operation']
    if action != 'update':
        if action == 'no_changed':
            return f'{SPACE}{key}: {value}{END}'
        elif action == 'added':
            return f'{ADD}{key}: {value}{END}'
        elif action == 'deleted':
            return f'{DEL}{key}: {value}{END}'
    elif action == 'recursion':
        return formatter(dict_)
    else:
        old_value, new_value = value
        return f'{DEL}{key}: {old_value}{END}' \
               f'{ADD}{key}: {new_value}{END}'


def formatter(lst):
    result = f'{OPEN_BRACKET}{END}'
    for item in lst:
        result += get_converting(item)
    result += CLOSE_BRACKET
    return result
