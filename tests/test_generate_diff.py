from os import path
from gendiff.generate_diff import generate_diff

file1_json = path.join(path.dirname("./tests/fixtures/"),
                       "file1.json")
file2_json = path.join(path.dirname("./tests/fixtures/"),
                       "file2.json")
result_simple_json = str(path.join(path.dirname("./tests/fixtures/expected/"),
                                   "json_stylish.txt"))


def simple_json():
    with open(result_simple_json) as result:
        assert generate_diff(file1_json, file2_json) == result.read()
