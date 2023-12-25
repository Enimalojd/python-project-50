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
    space = make_space(depth)
    bracket_space = make_space(depth, True)
    diff_lines = []
    for key, status in sorted(diff.items()):
        value = value_to_str(status.get('value'), depth)
        if status['operation'] == 'removed':
            diff_lines.append(f"{space}- {key}: {value}")
        elif status['operation'] == 'added':
            diff_lines.append(f"{space}+ {key}: {value}")
        elif status['operation'] == 'unchanged':
            diff_lines.append(f"{space}  {key}: {value}")
        elif status['operation'] == 'nested':
            nested_diff = format_stylish(status['value'], depth + 1)
            diff_lines.append(f"{space}  {key}: {nested_diff}")
        elif status['operation'] == 'changed':
            old_value = value_to_str(status['old'], depth)
            new_value = value_to_str(status['new'], depth)
            diff_lines.append(f"{space}- {key}: {old_value}")
            diff_lines.append(f"{space}+ {key}: {new_value}")

    joined_lines = '\n'.join(diff_lines)
    return f"{{\n{joined_lines}\n{bracket_space}}}"
