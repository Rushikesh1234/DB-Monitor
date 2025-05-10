from sqlalchemy import Column, Integer, String, DateTime
from app.db import Base
import datetime

class SlowQuery(Base):
    __tablename__ = "slow_queries"
    id = Column(Integer, primary_key=True, index=True)
    sql_id = Column(String)
    elapsed_time = Column(Integer)
    sql_text = Column(String)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

class LongTransactions(Base):
    __tablename__ = "long_transactions"
    id = Column(Integer, primary_key=True, index=True)
    sid = Column(Integer)
    serial = Column(Integer)
    username = Column(String)
    start_time = Column(DateTime)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
