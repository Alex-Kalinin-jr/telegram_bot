### TEMPLATE FOR TELEGRAM BOT SHOWING CATEGORIES AND POSITIONS OF ANYTHING PRESENTED IN DB.

- The bot is written on aiogram 3.7.
- It uses webhooks+FastApi for load descending
- Asyncsqlite is used for simplification, but architecture allows to replace with Postgres or something else in large projects, or event to pack the parts into containers.

Investigate **settings.ini.example**, make **settings.ini**, fill the database(example is in **database/db.py**) run **main.py** and enjoy.

If you want to deploy the bot on remote server, there are some helping files for that. **You can adjust them for your needs**:
- **Makefile** with ```make run``` to launch the script in background
- **launch.sh** with check script and relaunching instructions. Do not forget to add execute rights to script. Schedule execution. Example: you can adjust cron: Write ```crontab -e``` and insert the line ```0 * * * * /path/to/script/launch.sh >> /path/to/log/cron_log.log 2>&1```



***If you want dockerized version, switch to ```develop_docker``` branch (now in progress)***
