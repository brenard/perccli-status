lint:
	python3 -m flake8 perccli_status.py tests/
	python3 -m pylint perccli_status.py tests/

black:
	python3 -m black perccli_status.py tests/

test:
	python3 -m pytest

coverage:
	coverage run --source perccli_status -m pytest tests/ -x -vv
	coverage report --show-missing --fail-under 100
