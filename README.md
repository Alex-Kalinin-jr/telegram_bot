### TEMPLATE FOR TELEGRAM BOT.

#### System explanation

This application is microservice-architecture app, which is intended to show the data from database to user. It consist of: ***postgres_service*** with the database, ***db_service*** with the database wrapper and API, ***telegram_bot_service*** with the bot logic and API. For db convenience the ***adminer*** is included from db-side, the SQLModel + Alembic are included as ORM mapping. API is implemented via FastAPI. You can look at working version on:

<a href=https://web.telegram.org/a/#6998070759></a>

There are 2 branches: 



- The bot is written on aiogram 3.7.
- It uses webhooks+FastApi for load decreasing
- It uses postgres as database.

#### Working version of bot:


If you want to deploy the bot on remote server, there are some helping files for that. **You can adjust them for your needs**:
- **Makefile** with ```make run``` to launch the script in background
- **launch.sh** with check script and relaunching instructions. Do not forget to add execute rights to script. Schedule execution. Example: you can adjust cron: Write ```crontab -e``` and insert the line ```0 * * * * /path/to/script/launch.sh >> /path/to/log/cron_log.log 2>&1```



***If you want dockerized version, switch to ```develop_docker``` branch (now in progress)***
