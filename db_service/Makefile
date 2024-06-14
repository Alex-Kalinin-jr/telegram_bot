export PYTHONUNBUFFERED=1
export PYTHONPYCACHEPREFIX="/.cache/pycache/"

all: wait_for_it

wait_for_it: 
	chmod +x ./wait-for-it.sh 
	./wait-for-it.sh -t 120 $$POSTGRES_SERVICE_HOST:$$POSTGRES_SERVICE_PORT