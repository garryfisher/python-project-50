import json

OPEN_BRACKET = '{'
CLOSE_BRACKET = '}'
SPACE = '    '
ADD = '  + '
DEL = '  - '
END = '\n'


def get_indent(depth, mode='skip'):
    if mode == 'skip':
        return SPACE * depth
    elif mode == 'add':
        return SPACE * (depth - 1) + ADD
    elif mode == 'del':
        return SPACE * (depth - 1) + DEL


def get_readability(raw_data, depth):
    if isinstance(raw_data, list):
        result = raw_data
    elif isinstance(raw_data, dict):
        result = f'{OPEN_BRACKET}{END}'
        result += get_tree(raw_data, depth + 1)
        result += f'{get_indent(depth)}{CLOSE_BRACKET}'
    elif isinstance(raw_data, tuple):
        result = (get_readability(raw_data[0], depth),
                  get_readability((raw_data[1]), depth))
    else:
        result = json.dumps(raw_data).strip('"')

    return result


def get_tree(value, depth=0):
    tree = ''
    for tree_key, tree_value in value.items():
        if isinstance(tree_value, dict):
            tree += f'{get_indent(depth)}{tree_key}: {OPEN_BRACKET}{END}'
            tree += f'{get_tree(tree_value, depth + 1)}'
            tree += f'{get_indent(depth)}{CLOSE_BRACKET}{END}'
        else:
            tree_value = json.dumps(tree_value).strip('"')
            tree += f'{get_indent(depth)}{tree_key}: {tree_value}{END}'

    return tree


def stylish_format(diff, depth=1):
    result = f'{OPEN_BRACKET}{END}'
    for item in diff:
        key = item['key']
        value = get_readability(item['value'], depth)
        action = item['operation']
        if action == 'children':
            result += f"{get_indent(depth, 'skip')}{key}: "
            result += f"{stylish_format(value, depth+1)}{END}"
        elif action == 'added':
            result += f"{get_indent(depth, 'add')}{key}: {value}{END}"
        elif action == 'deleted':
            result += f"{get_indent(depth, 'del')}{key}: {value}{END}"
        elif action == 'updated':
            result += f"{get_indent(depth, 'del')}{key}: {value[0]}{END}"
            result += f"{get_indent(depth, 'add')}{key}: {value[1]}{END}"
        else:
            result += f"{get_indent(depth, 'skip')}{key}: {value}{END}"
    result += f"{get_indent(depth-1)}{CLOSE_BRACKET}"

    return result
