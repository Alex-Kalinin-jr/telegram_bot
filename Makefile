run:
	nohup python main.py > main_log.log 2>&1 &


# TO CHECK THE PROCESS IS LAUNCHING: ps aux | grep -v grep | grep main.py
# TO SCHEDULE RELAUNCHING WITH CRONTAB: 0 * * * * /home/alex/bltk_minibot/launch.sh >> /home/alex/bltk_minibot/cron_log.log 2>&1