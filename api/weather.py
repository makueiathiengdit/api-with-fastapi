from fastapi import APIRouter, Depends
from models import weather
from models.weather import CoverageCity
from service.weather_service import WeatherService
from api.db.connect import  get_db
from sqlalchemy.orm import Session



router  = APIRouter(prefix="/weather")

@router.get("/")
def get_weather(db:Session = Depends(get_db)):
    return WeatherService.get_all(db=db)


@router.get("/{city}")
def get_weather_by_city(city:CoverageCity, db:Session = Depends(get_db)):
    result = WeatherService.get_by_city(city, db=db)
    return result



# create weather record
@router.post("/")
def create_weather(weather:weather.Weather, db:Session = Depends(get_db)):
    item  = WeatherService.create_weather(weather, db=db)
    return item



#update weather 
@router.put("/{id}")
def update_weather(id:int, weather:weather.Weather, db:Session = Depends(get_db)):
    item = WeatherService.update_weather(id, weather, db=db)
    return item


# delete weather record
@router.delete("/{id}")
def delete_weather(id:int, db:Session=Depends(get_db)):
    res = WeatherService.delete_weather(id, db)
    
    return res
    
    
