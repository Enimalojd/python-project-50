def build_diff(data1, data2):
    diff = {}
    keys = sorted(data1.keys() | data2.keys())
    for key in keys:
        status = {'key': key}
        if key not in data2:
            status['operation'] = 'removed'
            status['value'] = data1[key]
        elif key not in data1:
            status['operation'] = 'added'
            status['value'] = data2[key]
        elif data1[key] == data2[key]:
            status['operation'] = 'unchanged'
            status['value'] = data2[key]
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            status['operation'] = 'nested'
            status['value'] = build_diff(data1[key], data2[key])
        else:
            status['operation'] = 'changed'
            status['old'] = data1[key]
            status['new'] = data2[key]
        diff[key] = status
    return diff
