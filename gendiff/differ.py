from .parser import read_file


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
        return f" + {key}: {value2}"
    elif value2 is None:
        return f" - {key}: {value1}"
    elif value1 == value2:
        return f"   {key}: {value1}"
    else:
        return f" - {key}: {value1}\n + {key}: {value2}"


def format_diff(diff):
    lines = [format_line(key, value1, value2) for key,
             (value1, value2) in sorted(diff.items())]
    result = "\n".join(lines)
    return "{\n" + result + "\n}"


def generate_diff(file_path1, file_path2):
    data1 = read_file(file_path1)
    data2 = read_file(file_path2)
    diff = compare_data(data1, data2)
    return format_diff(diff)
