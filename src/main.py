from src.utils.Sensor import Sensor

sensor = Sensor(4)

sensor.measure()
print(f'Temperature: {sensor.get_temperature()}')