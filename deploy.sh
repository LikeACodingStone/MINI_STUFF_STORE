#!/bin/bash
cd /home/LikeACodingStone/MINI_STUFF_STORE
git pull
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
touch /var/www/LikeACodingStone_pythonanywhere_com_wsgi.py 