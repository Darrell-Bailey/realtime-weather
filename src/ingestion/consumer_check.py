from kafka import KafkaConsumer
import json
import os

BOOTSTRAP = os.getenv("KAFKA_BOOTSTRAP", "host.docker.internal:9092")
TOPIC = os.getenv("KAFKA_TOPIC", "weather_raw")
GROUP = os.getenv("CONSUMER_GROUP", "check-group")

consumer = KafkaConsumer(
    TOPIC,
    bootstrap_servers=BOOTSTRAP,
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id=GROUP,
    value_deserializer=lambda v: json.loads(v.decode("utf-8")),
    consumer_timeout_ms=1000
)

if __name__ == "__main__":
    print("Consuming from topic:", TOPIC)
    for msg in consumer:
        print("offset=%s key=%s value=%s" % (msg.offset, msg.key, msg.value))
    print("No more messages right now.")