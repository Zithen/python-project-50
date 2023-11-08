import pytest
from gendiff.main_logic.gener_diff import generate_diff


FILE_JSON_PATH1 = 'tests/fixtures/file1.json'
FILE_JSON_PATH2 = 'tests/fixtures/file2.json'
FILE_YML_PATH1 = 'tests/fixtures/file1.yml'
FILE_YML_PATH2 = 'tests/fixtures/file2.yml'
FILE_YAML_PATH1 = 'tests/fixtures/file1.yaml'
FILE_YAML_PATH2 = 'tests/fixtures/file2.yaml'

RESULT_PATH = 'tests/fixtures/result_generate_diff.txt'


@pytest.fixture
def expected():
    with (open(RESULT_PATH) as expected):
        return ('').join(list(expected))


def test_json(expected):
    result = generate_diff(FILE_JSON_PATH1, FILE_JSON_PATH2)
    assert result == expected


def test_yml(expected):
    result = generate_diff(FILE_YML_PATH1, FILE_YML_PATH2)
    assert result == expected


def test_yaml(expected):
    result = generate_diff(FILE_YAML_PATH1, FILE_YAML_PATH2)
    assert result == expected
