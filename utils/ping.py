import requests
import time

def keep_alive():
    while True:
        try:
            requests.get('你的应用URL')
            time.sleep(14 * 60)  # 每14分钟ping一次
        except:
            pass 