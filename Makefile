-include .env
export

run:
	python -m cap

lint:
	@mypy cap
	@flake8 cap
