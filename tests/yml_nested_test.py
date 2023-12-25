import gendiff.differ as df


def test_compare_yml_files():
    path1 = 'tests/fixtures/file1_nested.yml'
    path2 = 'tests/fixtures/file2_nested.yml'
    result_path = 'tests/fixtures/result_nested_yml.txt'
    with open(result_path, 'r') as f:
        result = f.read().strip()
    assert df.generate_diff(path1, path2) == result
