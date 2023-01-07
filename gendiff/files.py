import json
import yaml
import os


def get_format(in_, formats):
    if formats == ".json":
        return json.load(in_)
    if formats == ".yml" or formats == ".yaml":
        return yaml.safe_load(in_)


def get_file(path_to_file):
    name, formats = os.path.splitext(os.path.normpath(path_to_file))
    with open(path_to_file) as file:
        return get_format(file, formats)
