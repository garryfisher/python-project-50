from gendiff.diff import get_diff
from gendiff.parser import loading
from gendiff.extension.stylish import get_stylish
from gendiff.extension.plain import get_plain
from gendiff.extension.json import get_json


FORMATS = {
    'stylish': get_stylish,
    'plain': get_plain,
    'json': get_json,
}


def generate_diff(path_to_file1, path_to_file2, format_type="stylish"):
    formatter = FORMATS[format_type]

    return formatter(get_diff(loading(path_to_file1),
                              loading(path_to_file2)))
