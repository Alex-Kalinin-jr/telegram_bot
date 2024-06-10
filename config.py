# - *- coding: utf- 8 - *-
import configparser

from apscheduler.schedulers.asyncio import AsyncIOScheduler

settings_configurator = configparser.ConfigParser()
settings_configurator.read("settings.ini")

BOT_TOKEN = settings_configurator['settings']['token'].strip()
BOT_TIMEZONE = settings_configurator['settings']['timezone'].strip()
BOT_VERSION = 1.0
PATH_DATABASE = settings_configurator['settings']['db_path']
PATH_LOGS = settings_configurator['settings']['logs_path']
LANGUAGE = settings_configurator['settings']['language']
NGROK_TOKEN = settings_configurator['settings']['ngrok_token'].strip()


def get_admins() -> list[int]:
    read_admins = configparser.ConfigParser()
    read_admins.read("settings.ini")

    admins = [admin.strip() for admin in read_admins['settings']['admin_id'].split(",")]
    admins = [int(admin) for admin in admins if admin]

    return admins