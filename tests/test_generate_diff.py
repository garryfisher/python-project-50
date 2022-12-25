from os import path
from gendiff.generate_diff import generate_diff

file1_json = path.join(path.dirname("./tests/fixtures/"),
                       "test_file1.json")
file2_json = path.join(path.dirname("./tests/fixtures/"),
                       "test_file2.json")
file1_yml = path.join(path.dirname("./tests/fixtures/"),
                      "test_file1.yml")
file2_yml = path.join(path.dirname("./tests/fixtures/"),
                      "test_file2.yml")
result_type_str = str(path.join(path.dirname("./tests/fixtures/"),
                                "test_result_json.txt"))


def test_generate_diff_json():
    with open(result_type_str) as result:
        assert generate_diff(file1_json, file2_json) == result.read()


def test_generate_diff_yml():
    with open(result_type_str) as result:
        assert generate_diff(file1_yml, file2_yml) == result.read()
