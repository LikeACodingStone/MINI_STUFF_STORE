#!/usr/bin/env bash
# 构建脚本
python -m pip install --upgrade pip
pip install -r requirements.txt

# 运行数据库迁移
python manage.py makemigrations
python manage.py migrate

# 收集静态文件
python manage.py collectstatic --no-input 