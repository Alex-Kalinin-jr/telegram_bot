FROM python:3.11-slim

WORKDIR /app
COPY . .

RUN apt update -y && apt upgrade -y
RUN apt install -y build-essential && apt autoclean -y && apt autoremove -y

EXPOSE 8000
