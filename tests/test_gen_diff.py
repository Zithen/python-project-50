import pytest
from gendiff.main_logic.gener_diff import generate_diff
import tests.fixtures.consts as CONSTS


@pytest.fixture
def expected():
    with (open(CONSTS.RESULT_PATH) as expected):
        return ('').join(list(expected))


def test_json(expected):
    result = generate_diff(CONSTS.FILE_JSON_PATH1, CONSTS.FILE_JSON_PATH2)
    assert result == expected


def test_yml(expected):
    result = generate_diff(CONSTS.FILE_YML_PATH1, CONSTS.FILE_YML_PATH2)
    assert result == expected


def test_yaml(expected):
    result = generate_diff(CONSTS.FILE_YAML_PATH1, CONSTS.FILE_YAML_PATH2)
    assert result == expected
