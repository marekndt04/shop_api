run:
	docker-compose run --rm web

tests:
	docker-compose run --rm web pytest $(args)

compile_deps:
	docker-compose run --rm web pip-compile