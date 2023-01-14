from fastapi import FastAPI, Query, HTTPException, status
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field
from typing import Optional, List, Dict
from database import cars

templates = Jinja2Templates(directory = "templates")


class Car(BaseModel):
    make: Optional[str]
    model: Optional[str]
    year: Optional[int] = Field(...,ge=1970,lt=2022)
    price: Optional[float]
    engine: Optional[str] = "V4"
    autonomous: Optional[bool]
    sold: Optional[List[str]]

app = FastAPI()

@app.get("/")
def root():
    return {"Welcome to": "your fisrt API in FastAPI"}

@app.get("/cars", response_model=List[Dict[str,Car]])
def get_cars(number: Optional[str] = Query("10", max_length=3)):
    reponse =[]
    for id, car in list(cars.items())[:int(number)]:
        to_add = {}
        to_add[id] = car
    reponse.append(to_add)