#!/bin/sh
# if virtualenvwrapper.sh is in your PATH (i.e. installed with pip)
source `which virtualenvwrapper.sh`
#source /path/to/virtualenvwrapper.sh # if it's not in your PATH
cd /home/hlsh/hl/hlsh_report

workon $1

nohup python manage.py runserver 0.0.0.0:8888 &
