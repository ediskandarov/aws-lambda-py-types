lint:
	poetry run mypy aws_lambda_types tests
	poetry run black aws_lambda_types tests --check
	poetry run isort --check-only aws_lambda_types tests
	poetry run flake8 aws_lambda_types tests

format:
	poetry run autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place aws_lambda_types tests --exclude=__init__.py
	poetry run black aws_lambda_types tests
	poetry run isort aws_lambda_types tests

test:
	poetry run pytest tests -vv
