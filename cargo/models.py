from sqlalchemy import Column, String, Integer, Text, DateTime, ForeignKey, Boolean, Date
from sqlalchemy.orm import relationship
from core.base import Base

class Cargo(Base):

    __tablename__ = "cargo"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    cargo_name = Column(String)
    weight = Column(Integer)
    description = Column(Text)
    created_at = Column(DateTime)
    # pick_up_location = fields.ForeignKeyField(
    #     'models.Location', related_name='pick_up', on_delete=fields.SET_NULL, null=True
    # )
    # delivery_location = fields.ForeignKeyField(
    #     'models.Location', related_name='delivery', on_delete=fields.SET_NULL, null=True
    # )

