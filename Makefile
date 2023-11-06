install:
	poetry install

run:
	poetry run gendiff /home/zithen/education/hexlet_python_projects/python-project-50/gendiff/files/file1.json /home/zithen/education/hexlet_python_projects/python-project-50/gendiff/files/file2.json

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gen_diff --cov-report xml

lint:
	poetry run flake8 gendiff/main_logic && poetry run flake8 gendiff/scripts

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	poetry build

.PHONY: install test lint selfcheck check build