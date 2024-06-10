.PHONY: all
all:

install-dev:
	apt-get update && apt-get install -y python3-venv
	python3 -m venv venv
	venv/bin/pip install -r requirements-dev.txt

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


install:
	mkdir -p $(DESTDIR)/usr/bin
	install -m0755 perccli_status.py $(DESTDIR)/usr/bin/perccli-status

install-build:
	apt-get update && apt-get install -y build-essential devscripts

build-deb:
	dpkg-buildpackage -us -uc --no-pre-clean
