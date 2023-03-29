start-dev-env:
	pip install debugpy==1.6.2
	docker-compose up -d --build

sc:
	autoflake . && black . && isort .

test:
	coverage run -m pytest -vv test

test-report:
	coverage combine
	coverage report
