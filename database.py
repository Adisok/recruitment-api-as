import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://gaxfqezkbwxogg:c3178226937803ffc48bbc043e1cd06bdcef075a48b9c99002695626804e3012@ec2-54-220-170-192.eu-west-1.compute.amazonaws.com:5432/d6oja2701au3ag"
    #os.getenv("SQLALCHEMY_DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

