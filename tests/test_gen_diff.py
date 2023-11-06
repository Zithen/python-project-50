import pytest
from gendiff.main_logic.gener_diff import generate_diff


FILE_PATH1 = 'tests/fixtures/file1.json'
FILE_PATH2 = 'tests/fixtures/file2.json'
RESULT_PATH = 'tests/fixtures/result_generate_diff.txt'


@pytest.fixture
def file_path1():
    return FILE_PATH1


@pytest.fixture
def file_path2():
    return FILE_PATH2


@pytest.fixture
def expected():
    with (open(RESULT_PATH) as expected):
        return ('').join(list(expected))


def test_basic(file_path1, file_path2, expected):
    result = generate_diff(file_path1, file_path2)
    assert result == expected
