init:
	pip install -U pipenv
	pipenv lock
	pipenv install --dev

test:
	pipenv run py.test --capture=no --cov-report term-missing --cov-report html --cov=mountapi tests/
