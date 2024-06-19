FROM python:3.11-slim

WORKDIR /app
COPY . .

RUN apt update -y && apt upgrade -y
RUN apt install -y make -y && apt autoclean -y && apt autoremove -y
RUN python3 -m pip install -r requirements.txt


EXPOSE 8000
EXPOSE 6379
