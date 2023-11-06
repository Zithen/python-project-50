import pytest
from gendiff.main_logic.gener_diff import generate_diff


@pytest.fixture
def file_path1():
    return 'tests/fixtures/files/file1.json'
def file_path2():
    return 'tests/fixtures/file2.json'
def expected():
    with (open('tests/fixtures/result_generate_diff.txt') as expected):
        return expected

def test_basic(file_path1, file_path2):
    result = generate_diff(file_path1, file_path2)
    assert generate_diff() == expected
