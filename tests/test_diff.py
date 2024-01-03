import os.path

import pytest

import gendiff.differ as df


@pytest.fixture(scope='function')
def test_dir():
    return os.path.dirname(os.path.abspath(__file__))


def test_compare_json_nested_files(test_dir):
    path1 = os.path.join(test_dir, 'fixtures/file1_nested.json')
    path2 = os.path.join(test_dir, 'fixtures/file2_nested.json')
    result_path = os.path.join(test_dir, 'fixtures/result_nested_json.txt')

    with open(result_path, 'r', encoding="utf-8") as f:
        result = f.read().strip()

    assert df.generate_diff(path1, path2) == result


def test_compare_yml_nested_files(test_dir):
    path1 = os.path.join(test_dir, 'fixtures/file1_nested.yml')
    path2 = os.path.join(test_dir, 'fixtures/file2_nested.yml')
    result_path = os.path.join(test_dir, 'fixtures/result_nested_yml.txt')

    with open(result_path, 'r', encoding="utf-8") as f:
        result = f.read().strip()

    assert df.generate_diff(path1, path2) == result


def test_plain_format(test_dir):
    path1 = os.path.join(test_dir, 'fixtures/file1_nested.json')
    path2 = os.path.join(test_dir, 'fixtures/file2_nested.json')
    result_path = os.path.join(test_dir, 'fixtures/result_plain.txt')

    with open(result_path, 'r', encoding="utf-8") as f:
        result = f.read().strip()

    assert df.generate_diff(path1, path2, 'plain') == result
