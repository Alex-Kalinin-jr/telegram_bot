up:
	sudo docker-compose up

down:
	sudo docker-compose down

rmbot:
	- sudo docker stop telegram_bot_service
	- sudo docker rm telegram_bot_service
	- sudo docker rmi bltk_minibot_bot_service

migratedb:
	-docker-compose exec educ_db_service alembic revision \
	--autogenerate -m "revision_number_$(REVISIONNUMBER)"
	-docker-compose exec educ_db_service alembic upgrade head

filldb:
	-docker-compose exec educ_db_service alembic upgrade head
	-docker-compose exec educ_db_service python3 filling_data.py