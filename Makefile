test:
	flake8 libnexmo --ignore=E501
	py.test --cov libnexmo/

.PHONY: test
