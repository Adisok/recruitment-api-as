from sqlalchemy import (
    Column,
    Date,
    Float,
    Integer,
    LargeBinary,
    SmallInteger,
    String,
    Table,
    Text,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import NullType

Base = declarative_base()
metadata = Base.metadata


class Content(Base):
    __tablename__ = "content"

    MessageID = Column(SmallInteger, primary_key=True)
    MessageText = Column(String(160), nullable=False)
    Counter = Column(Integer)


