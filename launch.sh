#!/bin/bash

# check if the script is running
if ps aux | grep -v grep | grep main.py > /dev/null
then
    echo "Script is running"
else
    nohup /home/alex/Python-3.11.1/python /home/alex/bltk_minibot/main.py > /home/alex/bltk_minibot/main_log.log 2>&1 &
fi

# DO NOT FORGET TO CHECK EXECUTION RIGHTS OF THE SCRIPT: chmod +x launch.sh