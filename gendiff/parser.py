import os
import json
import yaml


def read_file(file_path):
    '''Определние формата файла и обработка.'''
    root, ext = os.path.splitext(file_path)
    with open(file_path, 'r', encoding="utf-8") as f:
        if ext in ['.json']:
            data = json.load(f)
        elif ext in ['.yml', '.yaml']:
            data = yaml.safe_load(f)
        else:
            raise ValueError(f'Unsupported file extension: {ext}')
    return data
