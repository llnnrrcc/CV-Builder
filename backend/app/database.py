import os

from dotenv import load_dotenv #loads key value pairs into the environment so os can find them
from sqlalchemy import create_engine # create db connection URL
from sqlalchemy.orm import sessionmaker, declarative_base # units of work (queries, commits/ rollback), relational tables

load_dotenv()

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://cvapp:cvapp_dev_password@localhost:5432/cvapp",
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()