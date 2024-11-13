import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from models import Base

load_dotenv()

FSTR_DB_HOST = os.getenv("FSTR_DB_HOST")
FSTR_DB_LOGIN = os.getenv("FSTR_DB_LOGIN")
FSTR_DB_PASS = os.getenv("FSTR_DB_PASS")
FSTR_DB_NAME = os.getenv("FSTR_DB_NAME")

DATABASE_URL = f"postgresql://{FSTR_DB_LOGIN}:{FSTR_DB_PASS}@{FSTR_DB_HOST}/{FSTR_DB_NAME}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)