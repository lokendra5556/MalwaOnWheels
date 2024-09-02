from sqlalchemy.orm import Session

import schemas
from utils import hash
import models


#Create
def create_driver(db: Session, driver: schemas.DriverCreate):
    # create Hash of the password
    db_driver = models.Drivers(
        name= driver.name,
        gender= driver.gender,
        address= driver.address,
        dob= driver.dob,
        phone= driver.phone,
        email = driver.email,
        licenseNum= driver.licenseNum,
        carRegNum= driver.carRegNum,
        hashedPassword= hash(driver.password))
    
    db.add(db_driver)
    db.commit()
    db.refresh(db_driver)
    return db_driver

#Read
def get_drivers(db: Session, limit : int):
    return db.query(models.Drivers).limit(limit)

def get_driver_by_id(db: Session, driver_id: int):
    return db.query(models.Drivers).filter(models.Drivers.id == driver_id).first()


def get_driver_by_phone(db: Session, phone: str):
    return db.query(models.Drivers).filter(models.Drivers.phone == phone).first()

def get_driver_by_licenceNum(db: Session, licenseNum: str):
    return db.query(models.Drivers).filter(models.Drivers.licenseNum == licenseNum).first()

def get_driver_by_email(db: Session, email: str):
    return db.query(models.Drivers).filter(models.Drivers.email == email).first()
