from fastapi import FastAPI
import models
from database import SessionLocal, engine
from router_driver import router as router_driver
from router_passenger import router as router_passenger

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router_driver)
app.include_router(router_passenger)

# Dependency
def get_db(): 
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()