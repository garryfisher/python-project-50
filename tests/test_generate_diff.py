from os import path
from gendiff.generate_diff import generate_diff
import json

file1 = path.join(path.dirname("./tests/fixtures/"),
                  "test_file1.json")
file2 = path.join(path.dirname("./tests/fixtures/"),
                  "test_file2.json")
result_type_str = str(path.join(path.dirname("./tests/fixtures/"),
                                "test_result_json.txt"))

# print(json.load(open(file1, 'r')))


def test_generate_diff():
    with open(result_type_str) as result:
        assert generate_diff(file1, file2) != result.read()
