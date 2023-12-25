def make_space(depth, is_bracket=False):
    return ' ' * (depth * 4 + 2 - (2 if is_bracket else 0))


def value_to_str(value, depth):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    if isinstance(value, dict):
        result = []
        for key, val in value.items():
            space = make_space(depth + 1)
            str_value = value_to_str(val, depth + 1)
            result.append(f"{space}  {key}: {str_value}")
        line = '\n'.join(result)
        return f"{{\n{line}\n{make_space(depth)}  }}"
    return str(value)


def format_stylish(diff, depth=0):
    bracket_space = make_space(depth, True)
    diff_lines = [format_line(key, status, depth)
                  for key, status in sorted(diff.items())]
    joined_lines = '\n'.join(diff_lines)
    return f"{{\n{joined_lines}\n{bracket_space}}}"


def format_line(key, status, depth):
    space = make_space(depth)
    value = value_to_str(status.get('value'), depth)
    if status['operation'] == 'removed':
        return f"{space}- {key}: {value}"
    elif status['operation'] == 'added':
        return f"{space}+ {key}: {value}"
    elif status['operation'] == 'unchanged':
        return f"{space}  {key}: {value}"
    elif status['operation'] == 'nested':
        nested_diff = format_stylish(status['value'], depth + 1)
        return f"{space}  {key}: {nested_diff}"
    elif status['operation'] == 'changed':
        return format_changed(key, status, depth)


def format_changed(key, status, depth):
    space = make_space(depth)
    old_value = value_to_str(status['old'], depth)
    new_value = value_to_str(status['new'], depth)
    return f"{space}- {key}: {old_value}\n{space}+ {key}: {new_value}"
