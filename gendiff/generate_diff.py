from gendiff.diff import get_diff
from gendiff.files import get_file


def generate_diff(path_to_file1, path_to_file2):
    return get_diff(get_file(path_to_file1), get_file(path_to_file2))
