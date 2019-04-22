import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

Base = declarative_base()


class TimeCrawling(Base):
    """
    Time Crawling
    """
    __tablename__ = 'time_crawling'

    id = Column(Integer, primary_key=True)
    time_server = Column(String(20))
    create_at = Column(DateTime,
                       default=datetime.datetime.utcnow)
    modify_at = Column(DateTime, nullable=True)

    def __repr__(self):
        return f'<TimeCrawling(code={self.time_server}, region={self.create_at},\
             value={self.modify_at})>'


class Voting(Base):
    """
    Voting table schema
    """
    __tablename__ = 'voting'

    id = Column(Integer, primary_key=True)
    code = Column(String(45))
    region = Column(String(100))
    value1 = Column(String(20))
    value2 = Column(String(20))
    time_id = Column(Integer, ForeignKey(TimeCrawling.id))

    def __repr__(self):
        return f'<Voting(code={self.code}, region={self.region},\
             value={self.value})>'
