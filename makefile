build:
	docker-compose build

run:
	docker-compose run --rm --service-ports web

compile_reqs:
	docker-compose run --rm web pip-compile requirements/base.in
	docker-compose run --rm web pip-compile requirements/cloud.in
	docker-compose run --rm web pip-compile requirements/local.in
	docker-compose run --rm web pip-compile requirements/test.in

upgrade_reqs:
	docker-compose run --rm web sh -c "\
	pip-compile --upgrade requirements/base.in && \
	pip-compile --upgrade requirements/cloud.in && \
	pip-compile --upgrade requirements/local.in && \
	pip-compile --upgrade requirements/test.in"

test:
	docker-compose run --rm web ./run_tests.sh $(args)

linters:
	docker-compose run --rm web sh -c "black . && mypy ."
