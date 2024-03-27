from sqlalchemy import Column, String, Integer, Text, DateTime, ForeignKey, Boolean, Date, Float
from sqlalchemy.orm import relationship
from core.base import Base


class Location(Base):

    __tablename__ = "location"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    city = Column(String)
    state = Column(String)
    zip = Column(Integer)
    latitude = Column(Float)
    longitude = Column(Float)
    created_at = Column(DateTime)
