import json
IN_FILE1 = "- "
IN_FILE2 = "+ "
IN_FILES = "  "



def get_file(path_to_file):
    with open(path_to_file, 'r') as file:
        return file.read()


def generate_diff(dir1, dir2):
    file1 = dict(sorted(json.loads(get_file(dir1)).items()))
    file2 = dict(sorted(json.loads(get_file(dir2)).items()))
    all_keys = sorted(set(file1) | set(file2))
    result = '{\n'
    for x in all_keys:
        if x not in file2:
            result += IN_FILE1 + x + ': ' + str(file1[x]) + '\n'
        elif x not in file1:
            result += IN_FILE2 + x + ': ' + str(file2[x]) + '\n'
        elif x in file1 and file2:
            if file1[x] == file2[x]:
                result += IN_FILES + x + ': ' + str(file2[x]) + '\n'
            else:
                result += IN_FILE1 + x + ': ' + str(file1[x]) + '\n'
                result += IN_FILE2 + x + ': ' + str(file2[x]) + '\n'
    result += '}'
    return result
