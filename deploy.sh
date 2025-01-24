#!/bin/bash
cd /home/MINISTUFF/MINI_STUFF_STORE
git pull
source ~/.virtualenvs/mini_stuff_store_env/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
touch /var/www/MINISTUFF_pythonanywhere_com_wsgi.py 