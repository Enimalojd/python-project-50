import os.path

import pytest

import gendiff.differ as df


@pytest.fixture(scope='function')
def test_dir():
    return os.path.dirname(os.path.abspath(__file__))


@pytest.mark.parametrize(('file_path1', 'file_path2', 'result_path', 'format_type'), [
    ('fixtures/file1_nested.json', 'fixtures/file2_nested.json', 'fixtures/result_nested_json.txt', 'stylish'),
    ('fixtures/file1_nested.yml', 'fixtures/file2_nested.yml', 'fixtures/result_nested_yml.txt', 'stylish'),
    ('fixtures/file1_nested.json', 'fixtures/file2_nested.json', 'fixtures/result_plain.txt', 'plain')
])
def test_compare_data(test_dir, file_path1, file_path2, result_path, format_type):
    path1 = os.path.join(test_dir, file_path1)
    path2 = os.path.join(test_dir, file_path2)
    res_path = os.path.join(test_dir, result_path)

    with open(res_path, 'r', encoding='utf-8') as f:
        result = f.read().strip()

    assert df.generate_diff(path1, path2, format_type) == result