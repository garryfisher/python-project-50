import json
IN_FILE1 = "- "
IN_FILE2= "+ "
IN_FILES = "  "

file1 = json.load(open('./files/file1.json'))
file2 = json.load(open('./files/file2.json'))
file1 = dict(sorted(file1.items()))
file2 = dict(sorted(file2.items()))
file3 = sorted(set(file1) | set(file2))
file4 = {}

def generate_diff(path_to_file1, path_to_file2):
    result = {}
    for x in file3:
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
    print(result)


generate_diff(file1, file2)










