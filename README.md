## TEMPLATE FOR TELEGRAM BOT.

App for representing database data and interacting with it via telegram bot.

[Working version of bot is HERE](https://web.telegram.org/a/#6998070759)

- The bot is written on aiogram 3.7.
- It uses webhooks+FastApi for load decreasing
- It has ORM (SQLModel + Alembic)
- All interactions are asynchronous

#### System explanation

There are 2 versions of application:
1) branch **initial_template**. Template for investigation of bot structure. This is lightweighted version without docker. Database is realized via ***SQlite***. Bot internal storage is **MemoryStorage**.
All necessary **ENVIRONMENTS** are in **settings.ini** file

2) branch **main**. Microservice-architecture app, which is intended to show the data from database to user. It consist of: ***postgres_service*** with the database, ***db_service*** with the database wrapper and API, ***telegram_bot_service*** with the bot logic and API. For db convenience the ***adminer*** is included from db-side, the ***SQLModel + Alembic*** are included as ORM mapping. API is implemented via ***FastAPI***. Bot's memory storage is ***redis***
You can look at working version on:

Ok, to deploy this version:
 - Open ```docker-compose.yaml``` file and find locations of all ***.env*** files. Fill these files with apporpriate data. (For your convenience the ***.env.example*** is presented in each related place)
 - Hardcode your **ORM** in ```models.py```
 - Open ```db_service/alembic.ini``` and fill **line 62** by apporpriate data (**ALL APP USES ASYNCPG+POSTGRES AS ENGINE, YOU SHOULD USE AND SPECIFY EXACTLY IT**)
 - Launch ```make up```. This will set up containers. At this moment you have working app but empty database. So, let's fill it:
 launch ```make migratedb```.
 - Open adminer on ```localhost:8080```. You should see existing database with your tables. Fill themm by apporpriate data. Make database backup by ```make dump_postgres```. This will create sql filling script in **postgres_service** directory.
 - If you by any reason rebuild containers, just do ```make restore_postgres``` and enjoy.

