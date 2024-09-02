from pydantic import BaseModel
from datetime import date, time

# Driver

class Driver(BaseModel):
    id: int
    name: str
    gender: str
    phone: str
    carRegNum: str

class Passenger(BaseModel):
    id: int
    name: str
    gender: str
    phone: str

class DriverBase(BaseModel):
    name: str
    gender: str
    address: str
    dob: date
    phone: str
    email: str | None = None
    licenseNum: str
    carRegNum: str
    password: str


class DriverCreate(DriverBase):
    hashedPassword: str

    class Config:
        orm_mode = True


#passenger

class PassengerBase(BaseModel):
    name: str
    gender: str
    address: str
    dob: date
    phone: str
    email: str | None = None
    password: str

class PassengerCreate(PassengerBase):
    password: str

    class Config:
        orm_mode = True

#Trip

class TripBase(BaseModel):
    driverID: int
    passengerId1: int
    estPrice1: int
    pickUpLat1 : float
    pickUpLong1 : float
    dropLat1 : float
    dropLong1 : float
    estPickUpTime1: time
    estDropTime1: time
    date: date
    passengerCount: int

class TripCreate(TripBase):

    passengerId2: int | None = None
    passengerId3: int | None = None
    passengerId4: int | None = None
    estPrice2: int | None = None
    estPrice3: int | None = None
    estPrice4: int | None = None
    pickUpLat2 : float | None = None
    pickUpLong2 : float | None = None
    pickUpLat3 : float | None = None
    pickUpLong3 : float | None = None
    pickUpLat4 : float | None = None
    pickUpLong4 : float | None = None
    dropLat2 : float | None = None
    dropLong2 : float | None = None
    dropLat3 : float | None = None
    dropLong3 : float | None = None
    dropLat4 : float | None = None
    dropLong4 : float | None = None
    estPickUpTime2: time | None = None
    estPickUpTime3: time | None = None
    estPickUpTime4: time | None = None
    estDropTime2: time | None = None
    estDropTime3: time | None = None
    estDropTime4: time | None = None
    status: int | None = 0
    hashedOTP1: str
    hashedOTP2: str | None = None
    hashedOTP3: str | None = None
    hashedOTP4: str | None = None

    class Config:
        orm_mode = True


