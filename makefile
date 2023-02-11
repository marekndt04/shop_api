build:
	docker-compose build

run:
	docker-compose run --rm web

tests:
	docker-compose run --rm web pytest $(args)

compile_reqs:
	docker-compose run --rm web pip-compile requirements/base.in
	docker-compose run --rm web pip-compile requirements/local.in
	docker-compose run --rm web pip-compile requirements/test.in

upgrade_reqs:
	docker-compose run --rm web pip-compile --upgrade requirements/base.in
	docker-compose run --rm web pip-compile --upgrade requirements/local.in
	docker-compose run --rm web pip-compile --upgrade requirements/test.in

tests:
	docker-compose run --rm web ./test.sh

linters:
	docker-compose run --rm web sh -c "black . && mypy ."