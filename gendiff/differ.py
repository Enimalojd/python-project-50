from gendiff.build_diff import build_diff
from gendiff.formatter import format_selection
from gendiff.parser import get_data


def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1 = get_data(file_path1)
    data2 = get_data(file_path2)
    diff = build_diff(data1, data2)
    return format_selection(diff, format_name)
