# Produces synthetic sensor event to weather_raw every interval seconds

import json
import time
import uuid
from datetime import datetime
from kafka import KafkaProducer
import random
import os

BOOTSTRAP = os.getenv("KAFKA_BOOTSTRAP", "host.docker.internal:9092")
TOPIC = os.getenv("KAFKA_TOPIC", "weather_raw")
INTERVAL = int(os.getenv("SIM_INTERVAL_SEC", 5))

producer = KafkaProducer(
    bootstrap_servers=BOOTSTRAP,
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

def gen_sensor_event(sensor_id="sim-1"):
    return {
        "sensor_id": sensor_id,
        "event_id": str(uuid.uuid4()),
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "temperature_c": round(random.uniform(-5.0, 35.0), 2),
        "humidity": round(random.uniform(10, 95), 2),
        "wind_speed_ms": round(random.uniform(0, 20), 2),
        "source": "simulated"
    }
    
if __name__ == "__main__":
    print(f"Producing to {BOOTSTRAP} -> topic {TOPIC} every {INTERVAL}s")
    try:
        while True:
            print("Generating message...")
            msg = gen_sensor_event()
            try:
                producer.send(TOPIC, msg)
                producer.flush()
                print(f"Produced: {msg}")
            except Exception as e:
                print("Error producing message:", repr(e))
            time.sleep(INTERVAL)
    except KeyboardInterrupt:
        print("Stopping producer")
        producer.close()
    