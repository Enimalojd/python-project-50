import os
import json
import yaml


def get_data(file_path):
    root, ext = os.path.splitext(file_path)
    with open(file_path, 'r', encoding="utf-8") as f:
        return parse(f.read(), ext)


def parse(data, format):
    if format in ['.json']:
        return json.loads(data)
    elif format in ['.yml', '.yaml']:
        return yaml.safe_load(data)
    else:
        raise ValueError(f'Unsupported file extension: {format}')
