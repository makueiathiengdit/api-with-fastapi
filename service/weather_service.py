
from models.weather import Weather, CoverageCity
from api.db.models.weather import Weather as WeatherDBModel
from api.db.connect import get_db
from sqlalchemy.orm import Session
from fastapi import Depends
from typing import Annotated



db_dependency = Annotated[Session, Depends(get_db)]


class WeatherService:
    
    @classmethod
    def create_weather(cls, weather_data:Weather, db:db_dependency):
        weather_item = WeatherDBModel(**weather_data.dict())
        
        #convert city name to lowercase
        weather_item.city_name = weather_item.city_name.lower()
        db.add(weather_item)
        db.commit()
        db.refresh(weather_item)
        db.close()
        
        return weather_item
    
    @classmethod
    def update_weather(cls, id:int, weather_data:Weather, db:db_dependency):
        item_to_update = db.query(WeatherDBModel).filter(WeatherDBModel.id == id).first()
        
        if item_to_update:
            item_to_update.temperature = weather_data.temperature
            item_to_update.unit = weather_data.unit
            item_to_update.latitude = weather_data.latitude
            item_to_update.longitude = weather_data.longitude
            item_to_update.city_name = weather_data.city_name
            item_to_update.sunrise = weather_data.sunrise
            item_to_update.sunset = weather_data.sunset
            item_to_update.humidity = weather_data.humidity
            item_to_update.description = weather_data.description
            
            db.commit()
            db.refresh(item_to_update)
            db.close()
            
            return item_to_update
        
        return {"success":False, "message":"Item not found"}
    
    @classmethod
    def delete_weather(cls, id:int, db:db_dependency):
        item_to_delete = db.query(WeatherDBModel).filter(WeatherDBModel.id == id).first()
        
        if item_to_delete:
            db.delete(item_to_delete)
            db.commit()
            db.close()
            
            return {'success':True}
        
        return {'success':False}
    
    @classmethod
    def get_all(cls, db:Session):
        all_records = db.query(WeatherDBModel).all()
        return all_records or []
    
    @classmethod
    def get_by_city(cls, city:CoverageCity, db:db_dependency):
        
        # filter by city name and get lastest record
        res = db.query(WeatherDBModel).filter(WeatherDBModel.city_name == city).order_by(WeatherDBModel.created_at.desc()).first()
      
        return res or {}
       
        
    
    
    
    
    