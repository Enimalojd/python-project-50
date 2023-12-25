from .formatters.plain import format_plain
from .formatters.stylish import format_stylish
from .formatters.json import format_json


def format_selection(diff, format_name):
    if format_name == 'stylish':
        return format_stylish(diff)
    elif format_name == 'plain':
        return format_plain(diff)
    elif format_name == 'json':
        return format_json(diff)
