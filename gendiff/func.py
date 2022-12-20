def get_file(path_to_file):
    with open(path_to_file) as my_file:
        print(my_file.read())


get_file('/home/gennady/python-project-50/files/file1.json')