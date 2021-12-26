from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Restaurant(Base):
    __tablename__ = "restaurants"
    id_ = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    rating = Column(Float)
    lat = Column(Float, nullable=False)
    lon = Column(Float, nullable=False)