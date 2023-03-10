install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user --force-reinstall dist/*.whl

lint:
	poetry run flake8 gendiff

gendiff:
	poetry run gendiff

test:
	poetry run pytest

pytest-cov:
	pip install pytest-cov

test-coverage:
	poetry run pytest --cov --cov-report xml
