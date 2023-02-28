import json
import yaml


def load_data(data):
    if data.endswith('.json'):
        loader = json.load
    elif data.endswith('.yaml', '.yml'):
        loader = yaml.safe_load
    else:
        raise Exception('Unsupported file format')

    with open(data) as current_data:
        return loader(current_data)
