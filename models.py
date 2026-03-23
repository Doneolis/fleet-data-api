from sqlalchemy import Column, Integer, Float, Boolean
from database import engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class TripModel(Base):
    __tablename__ = "trips"

    id = Column(Integer, primary_key=True, index=True)
    truck_id = Column(Integer)
    distance = Column(Float)
    productive = Column(Boolean)

Base.metadata.create_all(bind=engine)