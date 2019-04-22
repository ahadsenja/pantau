import os

from sqlalchemy import create_engine

# engine = create_engine('sqlite:///pemilu.db')

MYSQL_PASSWORD = os.environ['MYSQL_PASSWORD']
engine = create_engine(f'mysql+mysqldb://root:{MYSQL_PASSWORD}@localhost:3306/pemilu2019')
