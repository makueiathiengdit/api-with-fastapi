from pydantic import BaseModel
from enum import Enum


class TemperatureUnit(str, Enum):
    celsius = "C"
    fahrenheit = "F"


class CoverageCity(str, Enum):
    juba = "Juba"
    rumbek = "Rumbek"
    yambio = "Yambio"
    bor = "Bor"
    wau = "Wau"
    malakal = "Malakal"
    torit = "Torit"
    bentiu = "Bentiu"
    yei = "Yei"
    
   

class Weather(BaseModel):
    temperature:float|None=0.0
    unit : TemperatureUnit | None = TemperatureUnit.celsius
    latitude : float | None = 24
    longitude :float | None = 14
    city_name : CoverageCity | None = CoverageCity.juba
    humidity:int | None = 0 
    sunrise:str|None = "5:30 AM"
    sunset:str|None = "6:35 PM"
    description:str|None=None