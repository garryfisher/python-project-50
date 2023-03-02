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
file1_tree_yaml = path.join(path.dirname("./tests/fixtures/"),
                            "file1_tree.yaml")
file2_tree_yaml = path.join(path.dirname("./tests/fixtures/"),
                            "file2_tree.yaml")

'''Expected'''
result_stylish = str(path.join(path.dirname("./tests/fixtures/expected/"),
                               "stylish.txt"))
result_plain = str(path.join(path.dirname("./tests/fixtures/expected/"),
                             "plain.txt"))
result_json = str(path.join(path.dirname("./tests/fixtures/expected/"),
                            "json.txt"))
result_stylish_tree = str(path.join(path.dirname("./tests/fixtures/expected/"),
                                    "tree_stylish.txt"))
result_plain_tree = str(path.join(path.dirname("./tests/fixtures/expected/"),
                                  "tree_plain.txt"))
result_json_tree = str(path.join(path.dirname("./tests/fixtures/expected/"),
                                 "tree_json.txt"))


def test_stylish_json():
    with open(result_stylish) as result:
        assert generate_diff(file1_json, file2_json) == result.read()


def test_stylish_yaml():
    with open(result_stylish) as result:
        assert generate_diff(file1_yaml, file2_yaml) == result.read()


def test_stylish_tree_json():
    with open(result_stylish_tree) as result:
        assert generate_diff(file1_tree_json, file2_tree_json) == result.read()


def test_stylish_tree_yaml():
    with open(result_stylish_tree) as result:
        assert generate_diff(file1_tree_yaml, file2_tree_yaml) == result.read()


def test_plain_json():
    with open(result_plain) as result:
        assert generate_diff(file1_json, file2_json, 'plain') == result.read()


def test_plain_yaml():
    with open(result_plain) as result:
        assert generate_diff(file1_yaml, file2_yaml, 'plain') == result.read()


def test_plain_tree_json():
    with open(result_plain_tree) as result:
        assert generate_diff(file1_tree_json, file2_tree_json, 'plain') == result.read()


def test_plain_tree_yaml():
    with open(result_plain_tree) as result:
        assert generate_diff(file1_tree_yaml, file2_tree_yaml, 'plain') == result.read()


def test_json_json():
    with open(result_json) as result:
        assert generate_diff(file1_json, file2_json, 'json') == result.read()


def test_json_yaml():
    with open(result_json) as result:
        assert generate_diff(file1_yaml, file2_yaml, 'json') == result.read()


def test_json_tree_json():
    with open(result_json_tree) as result:
        assert generate_diff(file1_tree_json, file2_tree_json, 'json') == result.read()


def test_json_tree_yaml():
    with open(result_json_tree) as result:
        assert generate_diff(file1_tree_yaml, file2_tree_yaml, 'json') == result.read()
