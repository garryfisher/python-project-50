from os import path
from gendiff.generate_diff import generate_diff

file1_json = path.join(path.dirname("./tests/fixtures/"),
                       "file1.json")
file2_json = path.join(path.dirname("./tests/fixtures/"),
                       "file2.json")
file1_yaml = path.join(path.dirname("./tests/fixtures/"),
                       "file1.yaml")
file2_yaml = path.join(path.dirname("./tests/fixtures/"),
                       "file2.yaml")
file1_tree_json = path.join(path.dirname("./tests/fixtures/"),
                            "file1_tree.json")
file2_tree_json = path.join(path.dirname("./tests/fixtures/"),
                            "file2_tree.json")
result_stylish = str(path.join(path.dirname("./tests/fixtures/expected/"),
                               "stylish.txt"))
result_json = str(path.join(path.dirname("./tests/fixtures/expected/"),
                            "json.txt"))
result_plain = str(path.join(path.dirname("./tests/fixtures/expected/"),
                             "plain.txt"))
result_stylish_tree = str(path.join(path.dirname("./tests/fixtures/expected/"),
                                    "tree_stylish.txt"))


def test_stylish_json():
    with open(result_stylish) as result:
        assert generate_diff(file1_json, file2_json) == result.read()


def test_plain_json():
    with open(result_plain) as result:
        assert generate_diff(file1_json, file2_json) == result.read()
#
#
# def test_json_json():
#     with open(result_json) as result:
#         assert generate_diff(file1_json, file2_json) == result.read()


# def test_stylish_json_tree():
#     with open(result_stylish_tree) as result:
#         assert generate_diff(file1_tree_json, file2_tree_json) == result.read()
