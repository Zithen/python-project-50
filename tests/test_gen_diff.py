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
def file_json_path1():
    return FILE_JSON_PATH1


@pytest.fixture
def file_json_path2():
    return FILE_JSON_PATH2


@pytest.fixture
def file_yml_path1():
    return FILE_YML_PATH1


@pytest.fixture
def file_yml_path2():
    return FILE_YML_PATH2


@pytest.fixture
def file_yaml_path1():
    return FILE_YAML_PATH1


@pytest.fixture
def file_yaml_path2():
    return FILE_YAML_PATH2


@pytest.fixture
def expected():
    with (open(RESULT_PATH) as expected):
        return ('').join(list(expected))


def test_json(file_json_path1, file_json_path2, expected):
    result = generate_diff(file_json_path1, file_json_path2)
    assert result == expected


def test_yml(file_yml_path1, file_yml_path2, expected):
    result = generate_diff(file_yml_path1, file_yml_path2)
    assert result == expected


def test_yaml(file_yaml_path1, file_yaml_path2, expected):
    result = generate_diff(file_yaml_path1, file_yaml_path2)
    assert result == expected
