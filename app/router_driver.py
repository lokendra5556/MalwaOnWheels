
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, APIRouter
import schemas
from database import SessionLocal
from utils import validateCarRegNum, validateEmail, validateLicenceNum, validateName, validatePhone
import crud_driver

crud = crud_driver
router = APIRouter()

# Dependency
def get_db(): 
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



#Create

# create a driver
@router.post("/driver/create/", response_model= schemas.Driver)
def create_driver(driver: schemas.DriverBase, db: Session = Depends(get_db)):

    #validate name
    if not validateName(driver.name) or driver.name == "string":
        raise HTTPException(status_code=400, detail="Check Name number")
    else:
        driver.name = driver.name.title().strip()

    #validate Phone number
    if not validatePhone(driver.phone) or driver.phone == "string":
        raise HTTPException(status_code=400, detail="Check phone number")
    
    #validate Email
    if driver.email != None:
        if not validateEmail(driver.email):
            raise HTTPException(status_code=400, detail="Check Email")

    #validate Licence number
    if not validateLicenceNum(driver.licenseNum) or driver.licenseNum == "string":
        raise HTTPException(status_code=400, detail="Check Licence number")

    #validate CarRegNum
    if not validateCarRegNum(driver.carRegNum) or driver.carRegNum == "string":
        raise HTTPException(status_code=400, detail="Check Car Registraion number")
    
    
    db_driver_phone = crud.get_driver_by_phone(db, phone=driver.phone)
    db_driver_lic = crud.get_driver_by_licenceNum(db, licenseNum=driver.licenseNum)
    db_driver_email = crud.get_driver_by_email(db, email= driver.email)

    # if phone number already exist return a message
    if db_driver_phone:
        raise HTTPException(status_code=400, detail="phone number already registered")
    # if licence number already exist return a message
    elif db_driver_lic:
        raise HTTPException(status_code=400, detail="Licence number already registered")
    elif db_driver_email:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_driver(db=db, driver=driver)

#Read

# get details of all drivers
@router.get("/drivers/", response_model=list[schemas.Driver])
def read_drivers(limit: int = 100, db: Session = Depends(get_db)):
    db_driver = crud.get_drivers(db, limit=limit)
    return db_driver


# get driver details by Phone number
@router.get("/driver/{phone}", response_model= schemas.Driver)
def read_driver_by_phone(phone: int, db: Session = Depends(get_db)):
    db_driver = crud.get_driver_by_phone(db, phone=phone)
    if db_driver is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_driver

# get driver details by id 
@router.get("/driver/{phone}", response_model= schemas.Driver)
def read_driver_by_phone(id: int, db: Session = Depends(get_db)):
    db_driver = crud.get_driver_by_id(db, id=id)
    if db_driver is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_driver