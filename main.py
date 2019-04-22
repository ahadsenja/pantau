from parser import Parser

from crawler import Crawler

if __name__ == "__main__":
    import sys
    import time

    TARGET_URL = 'https://pemilu2019.kpu.go.id/static/json/hhcw/ppwp.json'

    try:
        TIME_SLEEP = int(sys.argv[1])
    except ValueError as err:
        raise ValueError('TIME SLEEP must an Integer')

    while True:
        keeper = Crawler(TARGET_URL, verify_ssl=False)
        data = keeper.get_json_data()

        parser = Parser(data)
        result = parser.parse()

        print('Sent!')

        time.sleep(TIME_SLEEP)
