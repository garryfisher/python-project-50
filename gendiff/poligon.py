"""
Используется в качестве черновика
"""


def get_dir(file):
    file = str(file)
    name, formats = file.split('.')
    if formats == 'json' and name == 'file1':
        return './files/file1.json'
    if formats == 'json' and name == 'file2':
        return './files/file2.json'


print(get_dir('file1.json'))
