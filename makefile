build:
	docker-compose build

run:
	docker-compose run --rm web

tests:
	docker-compose run --rm web pytest $(args)

compile_deps:
	docker-compose run --rm web pip-compile requirements/base.in
	docker-compose run --rm web pip-compile requirements/local.in
	docker-compose run --rm web pip-compile requirements/test.in

upgrade_deps:
	docker-compose run --rm web pip-compile --upgrade requirements/base.in
	docker-compose run --rm web pip-compile --upgrade requirements/local.in
	docker-compose run --rm web pip-compile --upgrade requirements/test.in

linters:
	docker-compose run --rm web black .
	docker-compose run --rm web mypy .