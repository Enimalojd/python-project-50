import gendiff.differ as df


def test_plain_format():
    path1 = 'tests/fixtures/file1_nested.json'
    path2 = 'tests/fixtures/file2_nested.json'
    result_path = 'tests/fixtures/result_plain.txt'
    with open(result_path, 'r') as f:
        result = f.read().strip()
    assert df.generate_diff(path1, path2, 'plain') == result
