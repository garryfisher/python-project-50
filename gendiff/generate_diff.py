import json
IN_FILE1 = "- "
IN_FILE2 = "+ "
IN_FILES = "  "


def get_file(path_to_file):
    with open(path_to_file) as my_file:
        return my_file.read()


def generate_diff(first_file, second_file):
    dir1 = '/home/gennady/python-project-50/files/file1.json'
    dir2 = '/home/gennady/python-project-50/files/file2.json'
    # file_1 = json.loads(get_file(dir1))
    # file_2 = json.loads(get_file(dir2))
    file1 = dict(sorted(json.loads(get_file(dir1)).items()))
    file2 = dict(sorted(json.loads(get_file(dir2)).items()))
    all_keys = sorted(set(file1) | set(file2))
    result = {}
    for x in all_keys:
        if x not in file2:
            result[f'{IN_FILE1}{x}'] = file1[x]
        elif x not in file1:
            result[f'{IN_FILE2}{x}'] = file2[x]
        elif x in file1 and file2:
            if file1[x] == file2[x]:
                result[f'{IN_FILES}{x}'] = file2[x]
            else:
                result[f'{IN_FILE1}{x}'] = file1[x]
                result[f'{IN_FILE2}{x}'] = file2[x]
    return result
