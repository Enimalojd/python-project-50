import json
import pytest
import gendiff.differ as df


def test_compare_json_files():
    path1 = 'tests/fixtures/file1.json'
    path2 = 'tests/fixtures/file2.json'
    result_path = 'tests/fixtures/result_json.txt'
    
    with open(result_path, 'r') as f:
        result = f.read().strip()
       
    assert df.generate_diff(path1, path2) == result