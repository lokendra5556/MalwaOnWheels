
from sqlalchemy.orm import Session
from utils import hash
import models, schemas

# Create

def create_passenger(db: Session, passenger: schemas.PassengerCreate):
    db_passenger = models.Passengers(
        name= passenger.name,
        gender= passenger.gender,
        address= passenger.address,
        dob= passenger.dob,
        phone= passenger.phone,
        email = passenger.email,
        caringP1 = passenger.caringP1,
        caringP2 = passenger.caringP2,
        caringP3 = passenger.caringP3,
        cpPhone1 = passenger.cpPhone1,
        cpPhone2 = passenger.cpPhone2,
        cpPhone3 = passenger.cpPhone3,
        hashedPassword= hash(passenger.password))
    
    db.add(db_passenger)
    db.commit()
    db.refresh(db_passenger)
    return db_passenger

#Trip

def create_trip(db: Session, trip: schemas.TripCreate):
    fake_hashed_OTP1 = trip.hashedOTP1 + "notreallyhashed",
    fake_hashed_OTP2 = trip.hashedOTP2 + "notreallyhashed",
    fake_hashed_OTP3 = trip.hashedOTP3 + "notreallyhashed",
    fake_hashed_OTP4 = trip.hashedOTP4 + "notreallyhashed",

    db_trip = models.Trips(
        driverID = trip.driverID,
        passengerId1 = trip.passengerId1,
        estPrice1 = trip.estPrice1,
        pickUpLat1 = trip.pickUpLat1,
        pickUpLong1 = trip.pickUpLong1,
        dropLat1 = trip.dropLat1,
        dropLong1 = trip.dropLong1,
        estPickUpTime1= trip.estPickUpTime1,
        estDropTime1= trip.estDropTime1,
        date= trip.date,
        passengerCount= trip.passengerCount,
        passengerId2= trip.passengerId2,
        passengerId3= trip.passengerId3,
        passengerId4= trip.passengerId4,
        estPrice2= trip.estPrice2,
        estPrice3= trip.estPrice3,
        estPrice4= trip.estPrice4,
        pickUpLat2= trip.pickUpLat2,
        pickUpLong2= trip.pickUpLong1,
        pickUpLat3= trip.pickUpLat3,
        pickUpLong3= trip.pickUpLong3,
        pickUpLat4= trip.pickUpLat4,
        pickUpLong4= trip.pickUpLong4,
        dropLat2= trip.dropLat2,
        dropLong2= trip.dropLong2,
        dropLat3= trip.dropLat3,
        dropLong3= trip.dropLong3,
        dropLat4= trip.dropLat4,
        dropLong4= trip.dropLong4,
        estPickUpTime2= trip.estPickUpTime2,
        estPickUpTime3= trip.estPickUpTime3,
        estPickUpTime4= trip.estPickUpTime4,
        estDropTime2= trip.estDropTime2,
        estDropTime3= trip.estDropTime3,
        estDropTime4= trip.estDropTime4,
        status= trip.status,
        hashedOTP1= fake_hashed_OTP1,
        hashedOTP2= fake_hashed_OTP2,
        hashedOTP3= fake_hashed_OTP3,
        hashedOTP4= fake_hashed_OTP4
    )
    
    db.add(db_trip)
    db.commit()
    db.refresh(db_trip)
    return db_trip


def get_passenger(db: Session, passenger_id: int):
    return db.query(models.Passengers).filter(models.Passengers.id == passenger_id).first()


def get_passenger_by_phone(db: Session, phone: str):
    return db.query(models.Passengers).filter(models.Passengers.phone == phone).first()

def get_trips(db: Session, trip_id: int):
    return db.query(models.Trips).filter(models.Trips.id == trip_id).first()



# Update



# Delete