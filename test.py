from src.utils.Sensor import Sensor
import src.utils.WIFIsetup as wifi
import src.utils.MQTTsetup as mqtt
import time

# DHT11
sensor = Sensor(4)

# WIFI
wifi.connect()

# MQTT
client = mqtt.create()
client.connect()

while True:
    sensor.measure()
    client.publish('bedroom/temperature', f'{sensor.get_temperature()}')
    client.publish('bedroom/humidity', f'{sensor.get_humidity()}')
    time.sleep(1)
