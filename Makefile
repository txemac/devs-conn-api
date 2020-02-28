run:
	docker-compose up -d --build

tests: run
	docker-compose exec api pytest -vvv --pycodestyle .

stop:
	docker-compose stop

rm:
	docker-compose rm --stop -v --force
