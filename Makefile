test:
	flake8 libnexmo --ignore=E501
	py.test --cov libnexmo/

docs:
	cd docs && make html

.PHONY: test docs
