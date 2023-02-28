from gendiff.diff import get_diff
from gendiff.parser import load_data
from gendiff.extension.stylish import stylish_format


FORMATS = {
    'stylish': stylish_format,
}


def generate_diff(path_to_file1, path_to_file2, format_type='stylish'):
    formatter = FORMATS[format_type]

    return formatter(get_diff(load_data(path_to_file1),
                              load_data(path_to_file2)))
