up:
	sudo docker-compose up

down:
	sudo docker-compose down

rmbot:
	- sudo docker stop telegram_bot_service
	- sudo docker rm telegram_bot_service
	- sudo docker rmi bltk_minibot_bot_service