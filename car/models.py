from sqlalchemy import Column, String, Integer, Text, DateTime, ForeignKey, Boolean, Date, Float
from sqlalchemy.orm import relationship
from core.base import Base


class Car(Base):

    __tablename__ = "car"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    unique_number = Column(String)
    car_name = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    load_capacity = Column(Integer)
    created_at = Column(DateTime)


