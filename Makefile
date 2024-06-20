.PHONY: all
all:

install-dev: venv

venv:
	sudo apt-get update && sudo apt-get install -y python3-venv
	python3 -m venv venv
	venv/bin/pip install -r requirements-dev.txt

lint: venv
	venv/bin/python3 -m flake8 perccli_status.py tests/
	venv/bin/python3 -m pylint perccli_status.py tests/

black:
	venv/bin/python3 -m black perccli_status.py tests/

test:
	venv/bin/python3 -m pytest

coverage:
	venv/bin/coverage run --source perccli_status -m pytest tests/ -x -vv
	venv/bin/coverage report --show-missing --fail-under 95


install:
	install -m0755 perccli_status.py $(DESTDIR)/usr/sbin/perccli-status

install-build:
	sudo apt-get update && sudo apt-get install -y build-essential devscripts

build-deb:
	dpkg-buildpackage -us -uc --no-pre-clean
