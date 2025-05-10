from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import logging

logger = logging.getLogger(__name__)

USER = "admin"
PASSWORD = "password"
DSN = "host.docker.internal:1521/orclpdb1"

DATABASE_URL = f"oracle+oracledb://{USER}:{PASSWORD}@{DSN}"

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
