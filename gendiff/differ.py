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


def format_diff(diff):
    lines = []
    for key, (value1, value2) in sorted(diff.items()):
        if isinstance(value1, bool):
            value1 = str(value1).lower()
        if isinstance(value2, bool):
            value2 = str(value2).lower()
        if value1 is None:
            lines.append(f"+ {key}: {value2}")
        elif value2 is None:
            lines.append(f"- {key}: {value1}")
        elif value1 == value2:
            lines.append(f"  {key}: {value1}")
        else:
            lines.append(f"- {key}: {value1}\n+ {key}: {value2}")
    return "\n".join(lines)


def generate_diff(file_path1, file_path2):
    data1 = read_json(file_path1)
    data2 = read_json(file_path2)
    diff = compare_data(data1, data2)
    return print(format_diff(diff))


generate_diff(
    "D:/myProjects/python-project-50/tests/jsons/test1.json",
    "D:/myProjects/python-project-50/tests/jsons/test2.json",
)
