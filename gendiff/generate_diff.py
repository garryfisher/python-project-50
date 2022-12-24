import json
IN_FILE1 = "  - "
IN_FILE2 = "  + "
IN_FILES = "    "



def get_file(path_to_file):
    with open(path_to_file, 'r') as file:
        return file.read()


def get_dir(file):
    file = str(file)
    name, formats = file.split('.')
    if formats == 'json' and name == 'file1':
        return './files/file1.json'
    if formats == 'json' and name == 'file2':
        return './files/file2.json'


def generate_diff(in_1, in_2):
    dir1 = get_dir(in_1)
    dir2 = get_dir(in_2)
    file1 = dict(sorted(json.loads(get_file(dir1)).items()))
    file2 = dict(sorted(json.loads(get_file(dir2)).items()))
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
