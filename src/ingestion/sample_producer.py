import json
from datetime import datetime
from time import sleep

def gen_sample():
    return {
        "sensor_id": "sim-1",
        "timestamp": datetime.utcnow().isoformat() + "z",
        "temperature_c": 22.5,
        "humidity": 56.0,
        "wind_speed_ms": 3.2
    }
    
if __name__ == "__main__":
    for i in range(3):
        print(json.dumps(gen_sample()))
        sleep(1)