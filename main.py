from parser import Parser

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker

from connection import engine
from keeper import Keeper
from models import Base, TimeCrawling, Voting

if __name__ == "__main__":
    import sys
    import time

    # Generate database schema, check firrst if exists
    Base.metadata.create_all(engine, checkfirst=True)

    # Create new session
    Session = sessionmaker(bind=engine)
    session = Session()

    TARGET_URL = 'https://pemilu2019.kpu.go.id/static/json/hhcw/ppwp.json'

    try:
        TIME_SLEEP = int(sys.argv[1])
    except ValueError as err:
        raise ValueError('TIME SLEEP must an Integer')

    while True:
        keeper = Keeper(TARGET_URL, verify_ssl=False)
        data = keeper.get_json_data()

        parser = Parser(data)
        result = parser.parse()

        timec = TimeCrawling(time_server=result['ts'])
        session.add(timec)
        try:
            session.commit()

            for res in result['data']:
                res['time_id'] = timec.id
                voting = Voting(**res)
                session.add(voting)
                session.commit()
        except SQLAlchemyError as err:
            print(err)

        print('Created!')

        time.sleep(TIME_SLEEP)
