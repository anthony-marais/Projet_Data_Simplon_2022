import os, sys
from dotenv import load_dotenv
from sqlalchemy import create_engine
from app.db_commands import insert_db

def create_connection():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    load_dotenv(os.path.join(BASE_DIR, ".env"))
    sys.path.append(BASE_DIR)
    url = os.environ["DATABASE_URL"]
    engine = create_engine(url)
    return engine


connection = create_connection()

insert_db(connection)