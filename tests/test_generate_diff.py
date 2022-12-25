from os import path
from gendiff.generate_diff import generate_diff

file1 = path.join(path.dirname("./tests/fixtures/"),
                  "file1.json")
file2 = path.join(path.dirname("./tests/fixtures/"),
                  "file2.json")
result_type_str = str(path.join(path.dirname("./tests/fixtures/"),
                                "result_json.txt"))


# print(generate_diff(file1, file2))


def test_generate_diff():
    with open(result_type_str) as result:
        assert generate_diff(file1, file2) != result.read()
