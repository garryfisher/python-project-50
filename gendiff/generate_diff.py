import json
IS_FILE1 = "- "
IS_FILE2 = "+ "
IS_FILES = "  "


# in_file1 = json.load(open('/home/gennady/python-project-50/files/file1.json'))
# in_file2 = json.load(open('/home/gennady/python-project-50/files/file2.json'))


_file1 = {
  "host": "hexlet.io",
  "timeout": '50',
  "proxy": "123.234.53.22",
  "follow": 'false'
}
_file2 = {
  "timeout": '20',
  "verbose": 'true',
  "host": "hexlet.io"
}


def generate_diff(first_file, second_file):
    file1 = dict(sorted(first_file.items()))
    file2 = dict(sorted(second_file.items()))
    all_keys = sorted(set(file1) | set(file2))
    result = {}
    for x in all_keys:
        if x not in file2:
            result[f'{IS_FILE1}{x}'] = file1[x]
        elif x not in file1:
            result[f'{IS_FILE2}{x}'] = file2[x]
        elif x in file1 and file2:
            if file1[x] == file2[x]:
                result[f'{IS_FILES}{x}'] = file2[x]
            else:
                result[f'{IS_FILE1}{x}'] = file1[x]
                result[f'{IS_FILE2}{x}'] = file2[x]
    print(result)


generate_diff(_file1, _file2)
