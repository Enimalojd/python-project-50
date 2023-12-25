def value_to_str(value):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    if isinstance(value, str):
        return f"'{value}'"
    if isinstance(value, dict):
        return '[complex value]'
    return str(value)


def format_plain(diff, path=''):
    lines = []
    for key, status in diff.items():
        full_path = f"{path}.{key}" if path else key
        if status['operation'] == 'removed':
            lines.append(f"Property '{full_path}' was removed")
        elif status['operation'] == 'added':
            lines.append(f"Property '{full_path}' was added "
                         f"with value: "
                         f"{value_to_str(status['value'])}")
        elif status['operation'] == 'changed':
            old_value = value_to_str(status['old'])
            new_value = value_to_str(status['new'])
            lines.append(f"Property '{full_path}' was updated. "
                         f"From {old_value} to {new_value}")
        elif status['operation'] == 'nested':
            lines.append(format_plain(status['value'], full_path))
    return '\n'.join(lines)
