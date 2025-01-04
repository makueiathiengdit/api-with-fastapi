from sqlalchemy import Column, Integer, String, DateTime, Float

from api.db.connect import Base
import datetime

class Weather(Base):
    __tablename__ = "weather"
    id = Column(Integer, primary_key=True, autoincrement=True)
    temperature = Column(Float)
    unit = Column(String, default="C")
    latitude = Column(Float)
    longitude = Column(Float)
    city_name = Column(String)
    sunrise = Column(String)
    sunset = Column(String)
    humidity = Column(Integer)
    description = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.now)



