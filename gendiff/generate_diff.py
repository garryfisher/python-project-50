import json
import yaml
import os


OPENING_BRACKET = '{'
CLOSING_BRACKET = '}'
DEL = "  - "
ADD = "  + "
SPACE = "    "
END_STRING = '\n'


def get_format(in_, formats):
    if formats == ".json":
        return json.load(in_)
    if formats == ".yml" or formats == ".yaml":
        return yaml.safe_load(in_)


def get_file(path_to_file):
    name, formats = os.path.splitext(os.path.normpath(path_to_file))
    with open(path_to_file) as file:
        return get_format(file, formats)


def generate_diff(path_to_file1, path_to_file2):
    file1 = get_file(path_to_file1)
    file2 = get_file(path_to_file2)
    all_keys = sorted(set(file1.keys()) | set(file2.keys()))
    result = OPENING_BRACKET + END_STRING
    for x in all_keys:
        if x not in file2:
            result += f'{DEL}{x}: {file1[x]}' + END_STRING
        elif x not in file1:
            result += f'{ADD}{x}: {file2[x]}' + END_STRING
        elif x in file1 and file2:
            if file1[x] == file2[x]:
                result += f'{SPACE}{x}: {file2[x]}' + END_STRING
            else:
                result += f'{DEL}{x}: {file1[x]}' + END_STRING
                result += f'{ADD}{x}: {file2[x]}' + END_STRING
    result += CLOSING_BRACKET
    return result
