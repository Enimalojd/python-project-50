from gendiff.build_diff import build_diff
from gendiff.formatter import format_selection
from gendiff.parser import read_file


def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1 = read_file(file_path1)
    data2 = read_file(file_path2)
    diff = build_diff(data1, data2)
    return format_selection(diff, format_name)
