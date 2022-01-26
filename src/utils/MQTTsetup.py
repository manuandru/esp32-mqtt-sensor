from src.lib.umqttsimple import MQTTClient
from src.utils.config import MQTT
import ubinascii
import machine


def create():
    return MQTTClient(
        ubinascii.hexlify(machine.unique_id()),
        MQTT.broker,
        port=MQTT.port,
        user=MQTT.user,
        password=MQTT.password
    )