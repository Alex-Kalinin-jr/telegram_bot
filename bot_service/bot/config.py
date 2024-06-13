# - *- coding: utf- 8 - *-
import os
from dotenv import load_dotenv

load_dotenv()

TIMEZONE = os.getenv("TIMEZONE")

BOT_TOKEN = os.getenv("TOKEN")
NGROK_TOKEN = os.getenv("NGROK_TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID")
DB_PATH = os.getenv("DB_PATH")
LOGS_PATH = os.getenv("LOGS_PATH")
LANGUAGE = os.getenv("LANGUAGE")

AUTH_SERVICE = os.getenv("AUTH_SERVICE")



