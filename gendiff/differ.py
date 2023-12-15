import json


def read_json(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
    return data


def compare_data(data1, data2):
    diff = {}
    for key in data1.keys() | data2.keys():
        diff[key] = (data1.get(key), data2.get(key))
    return diff


def format_line(key, value1, value2):
    if isinstance(value1, bool):
        value1 = str(value1).lower()
    if isinstance(value2, bool):
        value2 = str(value2).lower()
    if value1 is None:
        return f"+ {key}: {value2}"
    elif value2 is None:
        return f"- {key}: {value1}"
    elif value1 == value2:
        return f"  {key}: {value1}"
    else:
        return f"- {key}: {value1}\n+ {key}: {value2}"


def format_diff(diff):
    lines = [format_line(key, value1, value2) for key,
             (value1, value2) in sorted(diff.items())]
    return "\n".join(lines)


def generate_diff(file_path1, file_path2):
    data1 = read_json(file_path1)
    data2 = read_json(file_path2)
    diff = compare_data(data1, data2)
    return format_diff(diff)