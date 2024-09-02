
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, APIRouter
from utils import validateEmail, validateName, validatePhone
import schemas
import crud_passenger
from database import SessionLocal

crud = crud_passenger
router = APIRouter()

# Dependency
def get_db(): 
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#Create

# create a passenger, if phone number already exists return message
@router.post("/passenger/create/", response_model= schemas.Passenger)
def create_passenger(passenger: schemas.PassengerCreate, db: Session = Depends(get_db)):

     #validate name
    if not validateName(passenger.name):
        raise HTTPException(status_code=400, detail="Check Name number")
    else:
        passenger.name = passenger.name.title().strip()

    #validate Phone number
    if not validatePhone(passenger.phone):
        raise HTTPException(status_code=400, detail="Check phone number")
    
    #validate Email
    if passenger.email != None:
        if not validateEmail(passenger.email):
            raise HTTPException(status_code=400, detail="Check Email")

    db_passenger = crud.get_passenger(db, phone=passenger.phone)
    if db_passenger:
        raise HTTPException(status_code=400, detail="phone number already registered")
    return crud.create_user(db=db, passenger=passenger)



# get all passengers
@router.get("/passengers/", response_model=list[schemas.Passenger])
def read_passengers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_passenger = crud.get_passenger(db, skip=skip, limit=limit)
    return db_passenger


# get passenger details by Phone number
@router.get("/passenger/{phone}", response_model= schemas.Passenger)
def read_passenger_by_phone(phone: int, db: Session = Depends(get_db)):
    db_passenger = crud.get_passenger_by_phone(db, phone=phone)
    if db_passenger is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_passenger