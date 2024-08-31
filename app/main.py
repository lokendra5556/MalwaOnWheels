from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from utils import validatePhone, validateCarRegNum, validateEmail, validateName

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()



# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#Driver

#Create

# create a driver, if phone number already exists return message
@app.post("/driver/create/", response_model= schemas.Driver)
def create_driver(driver: schemas.DriverBase, db: Session = Depends(get_db)):

    if driver.phone == "string":
        driver.phone = None
    if driver.licenseNum == "string":
        driver.licenseNum = None
    if driver.carRegNum == "string":
        driver.carRegNum = None

    #validate name
    if not validateName(driver.name):
        raise HTTPException(status_code=400, detail="Check Name number")
    else:
        driver.name = driver.name.title().strip()

    #validate Phone number
    if not validatePhone(driver.phone):
        raise HTTPException(status_code=400, detail="Check phone number")

    #validate CarRegNum
    if not validateCarRegNum(driver.carRegNum):
        raise HTTPException(status_code=400, detail="Check Car Registraion number")
    
    #validate Email
    if driver.email != None:
        if not validateEmail(driver.email):
            raise HTTPException(status_code=400, detail="Check Email")
    
    db_driver_phone = crud.get_driver_by_phone(db, phone=driver.phone)
    db_driver_lic = crud.get_driver_by_licenceNum(db, licenseNum=driver.licenseNum)

    if db_driver_phone:
        raise HTTPException(status_code=400, detail="phone number already registered")
    elif db_driver_lic:
        raise HTTPException(status_code=400, detail="Licence number already registered")
    return crud.create_driver(db=db, driver=driver)

#Read

# get details of all drivers
@app.get("/drivers/", response_model=list[schemas.Driver])
def read_drivers(limit: int = 100, db: Session = Depends(get_db)):
    db_driver = crud.get_drivers(db, limit=limit)
    return db_driver


# get driver details by Phone number
@app.get("/driver/{phone}", response_model= schemas.Driver)
def read_driver_by_phone(phone: int, db: Session = Depends(get_db)):
    db_driver = crud.get_driver_by_phone(db, phone=phone)
    if db_driver is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_driver

# get driver details by id 
@app.get("/driver/{phone}", response_model= schemas.Driver)
def read_driver_by_phone(id: int, db: Session = Depends(get_db)):
    db_driver = crud.get_driver_by_id(db, id=id)
    if db_driver is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_driver

#Passenger

#Create

# create a passenger, if phone number already exists return message
@app.post("/passenger/create/", response_model= schemas.Passenger)
def create_passenger(passenger: schemas.PassengerCreate, db: Session = Depends(get_db)):
    db_passenger = crud.get_passenger(db, phone=passenger.phone)
    if db_passenger:
        raise HTTPException(status_code=400, detail="phone number already registered")
    return crud.create_user(db=db, passenger=passenger)



# get all passengers
@app.get("/passengers/", response_model=list[schemas.Passenger])
def read_passengers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_passenger = crud.get_passenger(db, skip=skip, limit=limit)
    return db_passenger



# get passenger details by Phone number
@app.get("/passenger/{phone}", response_model= schemas.Passenger)
def read_passenger_by_phone(phone: int, db: Session = Depends(get_db)):
    db_passenger = crud.get_passenger_by_phone(db, phone=phone)
    if db_passenger is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_passenger