install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv test_0.py

format:	
	black *.py dblib/*py

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py

all: install lint test
