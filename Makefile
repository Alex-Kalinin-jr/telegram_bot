up:
	sudo docker-compose up

down:
	sudo docker-compose down

rmbot:
	- sudo docker stop telegram_bot_service
	- sudo docker rm telegram_bot_service
	- sudo docker rmi telegram_bot_bot_service

rmdb:
	- sudo docker stop db_service
	- sudo docker rm db_service
	- sudo docker rmi telegram_bot_db_service

migratedb:
	-sudo docker-compose exec db_service alembic revision \
	--autogenerate -m "revision_number_$(REVISIONNUMBER)"

upgrade:
	-sudo docker-compose exec db_service alembic upgrade head

filldb:
	-sudo docker-compose exec db_service alembic upgrade head
	-sudo docker-compose exec db_service python3 filling_data.py

clean: rmbot rmdb

upfill: up filldb

dump_postgres:
	docker exec -i postgres_service /bin/bash -c "PGPASSWORD=postgres pg_dump --username postgres postgres" > ./postgres_service/dump.sql

restore_postgres:
	docker exec -i postgres_service /bin/bash -c "PGPASSWORD=postgres psql --username postgres postgres" < ./postgres_service/dump.sql