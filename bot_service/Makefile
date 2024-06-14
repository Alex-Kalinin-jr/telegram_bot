export PYTHONUNBUFFERED=1
export PYTHONPYCACHEPREFIX=/.cache/pycache/

all: wait_for_it run

wait_for_it: 
	chmod +x ./wait-for-it.sh 
	./wait-for-it.sh -t 120 redis_service:6379

run:
	python3 bot/main.py