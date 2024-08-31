from sqlalchemy import Boolean, Column, ForeignKey, VARCHAR, CHAR, INT, SMALLINT, DOUBLE_PRECISION, TIME, DATE, TIMESTAMP
from sqlalchemy import func
from database import Base


class Drivers(Base):
    __tablename__ = "drivers"

    id = Column(INT, primary_key=True, unique= True, autoincrement=True, index= True)
    name = Column(VARCHAR(30), nullable=False)
    gender = Column(CHAR, nullable=False)
    dob = Column(DATE, nullable= False)
    address = Column(VARCHAR(100), nullable=False)
    phone = Column(VARCHAR(10), nullable= False, unique=True, index=True)
    email = Column(VARCHAR(50),unique=True,nullable=True, index=True)
    licenseNum = Column(VARCHAR(18), unique= True, nullable= False)
    carRegNum = Column(VARCHAR(10), unique= True, nullable= False)
    rating = Column(SMALLINT, nullable= True)
    tripCount = Column(INT, nullable= False, default= 0)
    hashedPassword = Column(VARCHAR(60), nullable=False)
    is_active = Column(Boolean, default=True, nullable= False)
    createdAt = Column(TIMESTAMP, default= func.now())

class Passengers(Base):
    __tablename__ = "passengers"

    id= Column(INT, primary_key= True, unique= True, autoincrement=True, index= True)
    name= Column(VARCHAR(30), nullable=False)
    gender= Column(CHAR, nullable=False)
    address= Column(VARCHAR(100), nullable=False)
    dob= Column(DATE, nullable= False)
    phone= Column(VARCHAR(10), nullable= False, unique=True, index=True)
    email= Column(VARCHAR(50),unique=True,nullable=True, index=True)
    caringP1= Column(VARCHAR(50), unique= False, nullable= True)
    caringP2= Column(VARCHAR(50), unique= False, nullable= True)
    caringP3= Column(VARCHAR(50), unique= False, nullable= True)
    cpPhone1= Column(VARCHAR(10), nullable= True, unique=False)
    cpPhone2= Column(VARCHAR(10), nullable= True, unique=False)
    cpPhone3= Column(VARCHAR(10), nullable= True, unique=False)
    rating= Column(SMALLINT, nullable= True)
    hashedPassword = Column(VARCHAR(60), nullable=False)
    is_active = Column(Boolean, default=True, nullable= False)
    createdAt = Column(TIMESTAMP, default= func.now())

class Trips(Base):
    __tablename__ = "trips"

    id= Column(INT, primary_key= True, unique= True, autoincrement= True, index= True)
    driverId = Column(INT, nullable= False, index= True)
    passengerId1= Column(INT, nullable= False)
    passengerId2= Column(INT)
    passengerId3= Column(INT)
    passengerId4= Column(INT)
    estPrice1= Column(INT, nullable= False)
    estPrice2= Column(INT)
    estPrice3= Column(INT)
    estPrice4= Column(INT)
    pickUpLat1= Column(DOUBLE_PRECISION, nullable= False)
    pickUpLong1= Column(DOUBLE_PRECISION, nullable= False)
    pickUpLat2= Column(DOUBLE_PRECISION, nullable= False)
    pickUpLong2= Column(DOUBLE_PRECISION, nullable= False)
    pickUpLat3= Column(DOUBLE_PRECISION, nullable= False)
    pickUpLong3= Column(DOUBLE_PRECISION, nullable= False)
    pickUpLat4= Column(DOUBLE_PRECISION, nullable= False)
    pickUpLong4= Column(DOUBLE_PRECISION, nullable= False)
    dropLat1= Column(DOUBLE_PRECISION, nullable= False)
    dropLong1= Column(DOUBLE_PRECISION, nullable= False)
    dropLat2= Column(DOUBLE_PRECISION, nullable= False)
    dropLong2= Column(DOUBLE_PRECISION, nullable= False)
    dropLat3= Column(DOUBLE_PRECISION, nullable= False)
    dropLong3= Column(DOUBLE_PRECISION, nullable= False)
    dropLat4= Column(DOUBLE_PRECISION, nullable= False)
    dropLong4= Column(DOUBLE_PRECISION, nullable= False)
    estPickUpTime1= Column(TIME, nullable= False)
    estPickUpTime2= Column(TIME)
    estPickUpTime3= Column(TIME)
    estPickUpTime4= Column(TIME)
    estDropTime1= Column(TIME, nullable= False)
    estDropTime2= Column(TIME)
    estDropTime3= Column(TIME)
    estDropTime4= Column(TIME)
    passengerCount= Column(SMALLINT)
    date= Column(DATE, nullable= False)
    status= Column(SMALLINT, nullable= False, default= 0)
    hashedOTP1= Column(VARCHAR(60), nullable=False)
    hashedOTP2= Column(VARCHAR(60))
    hashedOTP3= Column(VARCHAR(60))
    hashedOTP4= Column(VARCHAR(60))
    createdAt = Column(TIMESTAMP, default= func.now())












