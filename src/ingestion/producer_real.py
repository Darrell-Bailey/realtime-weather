import json
import time
import os
from datetime import datetime
import requests
from kafka import KafkaProducer

BOOTSTRAP = os.getenv("KAFKA_BOOTSTRAP", "localhost:9092")
TOPIC = os.getenv("KAFKA_TOPIC", "weather_raw")
LAT = os.getenv("LAT", "40.71")     # default: New York City
LON = os.getenv("LON", "-74.01")
INTERVAL = int(os.getenv("POLL_INTERVAL_SEC", "30"))

producer = KafkaProducer(
    bootstrap_servers=BOOTSTRAP,
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

def fetch_open_meteo(lat, lon):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    r = requests.get(url, timeout=10)
    r.raise_for_status()
    data = r.json()
    cw = data.get("current_weather", {})
    return {
        "sensor_id":f"open-meteo-{lat}-{lon}",
        "event_id":f"openmeteo-{int(datetime.utcnow().timestamp())}",
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "temperature_c": cw.get("temperature"),
        "wind_speed_ms": cw.get("windspeed"),
        "wind_direction_deg": cw.get("winddirection"),
        "weather_code": cw.get("weathercode"),
        "source": "open-meteo",
        "raw": cw
    }
    
if __name__ == "__main__":
    print(f"Polling Open-Meteo {LAT},{LON} -> producing to {TOPIC}")
    try:
        while True:
            ev = fetch_open_meteo(LAT, LON)
            producer.send(TOPIC, ev)
            producer.flush()
            print("Produced:", ev)
            time.sleep(INTERVAL)
    except KeyboardInterrupt:
        print("Stopping")
        producer.close()

