import os
import json
import yaml

def read_file(file_path):
    root, ext = os.path.splitext(file_path)
    with open(file_path, 'r') as f:
        if ext in ['.json']:
            data = json.load(f)
        elif ext in ['.yml', '.yaml']:
            data = yaml.safe_load(f)
        else:
            raise ValueError(f'Unsupported file extension: {ext}')
    return data