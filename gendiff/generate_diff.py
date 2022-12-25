import json
import yaml
import os


IN_FILE1 = "  - "
IN_FILE2 = "  + "
IN_FILES = "    "


def get_format(in_, formats):
    if formats == ".json":
        return json.load(in_)
    if formats == ".yml" or formats == ".yaml":
        return yaml.load(in_)


def get_file(path_to_file):
    name, formats = os.path.splitext(os.path.normpath(path_to_file))
    with open(path_to_file) as file:
        return get_format(file, formats)


def generate_diff(path_to_file1, path_to_file2):
    file1 = dict(sorted(get_file(path_to_file1).items()))
    file2 = dict(sorted(get_file(path_to_file2).items()))
    all_keys = sorted(set(file1) | set(file2))
    result = '{\n'
    for x in all_keys:
        if x not in file2:
            result += f'{IN_FILE1}{x}: {file1[x]}' + '\n'
        elif x not in file1:
            result += f'{IN_FILE2}{x}: {file2[x]}' + '\n'
        elif x in file1 and file2:
            if file1[x] == file2[x]:
                result += f'{IN_FILES}{x}: {file2[x]}' + '\n'
            else:
                result += f'{IN_FILE1}{x}: {file1[x]}' + '\n'
                result += f'{IN_FILE2}{x}: {file2[x]}' + '\n'
    result += '}'
    return result
