from fastapi import FastAPI
from pydantic import BaseModel
from database import SessionLocal
from models import TripModel

app = FastAPI()

trips = []

class Trip(BaseModel):
    truck_id: int
    distance: float
    productive: bool

class TripResponse(BaseModel):
    id: int
    truck_id: int
    distance: float
    productive: bool

    class Config:
        orm_mode = True

@app.post("/trips")
def create_trip(trip: Trip):
    db = SessionLocal()
    try:
        new_trip = TripModel(
            truck_id=trip.truck_id,
            distance=trip.distance,
            productive=trip.productive
        )

        db.add(new_trip)
        db.commit()
        db.refresh(new_trip)

        return {"message": "Trip created"}
    finally:
        db.close()

@app.get("/trips", response_model=list[TripResponse])
def get_trips():
    db = SessionLocal()
    try:
        trips = db.query(TripModel).all()
        return trips
    finally:
        db.close()