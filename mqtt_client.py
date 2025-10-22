import os
import paho.mqtt.client as mqtt
from .data_source import data_source_instance

BROKER = os.getenv("MQTT_BROKER", "broker.hivemq.com")
PORT = int(os.getenv("MQTT_PORT", "1883"))
PREFIX = os.getenv("MQTT_TOPICS_PREFIX", "compostech")

SUBSCRIPTIONS = [
    (f"{PREFIX}/+/data/temperature", 0),
    (f"{PREFIX}/+/data/humidity", 0),
    (f"{PREFIX}/+/data/ph", 0),
    (f"{PREFIX}/+/data/gas", 0),
    (f"{PREFIX}/+/alert/odor", 1),
    (f"{PREFIX}/+/alert/ph", 1),
    # Compatibilidade com tópicos sem deviceId
    (f"{PREFIX}/data/temperature", 0),
    (f"{PREFIX}/data/humidity", 0),
    (f"{PREFIX}/data/ph", 0),
    (f"{PREFIX}/data/gas", 0),
    (f"{PREFIX}/alert/odor", 1),
    (f"{PREFIX}/alert/ph", 1),
]

def _last_segment(topic: str) -> str:
    return topic.split("/")[-1]

def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    key = _last_segment(msg.topic)
    try:
        if key in ("temperature", "humidity", "ph"):
            val = float(payload)
        elif key == "gas":
            val = int(payload)
        else:
            val = payload
    except Exception:
        val = payload

    if key in ("temperature", "humidity", "ph", "gas"):
        data_source_instance.update_sensor(key, val)
    elif key in ("odor", "ph"):
        label = "pH Alert" if key == "ph" else "Odor Alert"
        data_source_instance.add_alert(f"{label}: {payload}")

def start_loop():
    client = mqtt.Client(os.getenv("MQTT_CLIENT_ID", "compostech-backend"))
    user = os.getenv("MQTT_USERNAME")
    pwd = os.getenv("MQTT_PASSWORD")
    if user and pwd:
        client.username_pw_set(user, pwd)
    client.on_message = on_message
    client.connect(BROKER, PORT, 60)
    for topic, qos in SUBSCRIPTIONS:
        client.subscribe((topic, qos))
    client.loop_forever()