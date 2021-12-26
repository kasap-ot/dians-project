import os
from sqlalchemy import create_engine
from dotenv import load_dotenv


# --------- Setup data ---------
load_dotenv(".env")
db_url = os.environ["DB_URL"]
engine = create_engine(db_url, echo=True)
connection = engine.connect()