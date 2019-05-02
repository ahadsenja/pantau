from parser import Parser

from crawler import Crawler
from sender import Sender

if __name__ == "__main__":
    import os
    import sys
    import time
    from datetime import datetime

    TARGET_URL = 'https://pemilu2019.kpu.go.id/static/json/hhcw/ppwp.json'
    API_URL = 'https://pantausintungkpu.web.id/api/pemilu2019/save'
    AUTH_TOKEN = os.environ['AUTH_TOKEN']

    try:
        TIME_SLEEP = int(sys.argv[1])
    except ValueError as err:
        raise ValueError('TIME SLEEP must an Integer')

    while True:
        crawler = Crawler(TARGET_URL, verify_ssl=False)
        data = crawler.get_json_data()

        parser = Parser(data)
        res_data = parser.parse()

        # print(res_data)
        sender = Sender(API_URL, AUTH_TOKEN)
        req = sender.send(res_data)

        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}, Code {req.status_code}")

        time.sleep(TIME_SLEEP)
