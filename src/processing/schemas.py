from pydantic import BaseModel, validator
from typing import Optional
from datetime import datetime

class WeatherEvent(BaseModel):
    event_id: str
    sensor_id: str
    timestamp: datetime
    source: str
    ingested_at: datetime
    temperature_c: Optional[float] = None
    humidity: Optional[float] = None
    wind_speed_ms: Optional[float] = None
    wind_direction_deg: Optional[float] = None
    weather_code: Optional[int] = None
    lat: Optional[float] = None
    lon: Optional[float] = None
    dew_point_c: Optional[float] = None
    
@validator("ingested_at", pre=True, always=True)
def set_ingested_at(cls, v):
    return v or datetime.utcnow()

