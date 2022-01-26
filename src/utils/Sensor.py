import dht
from machine import Pin
from time import sleep

class Sensor:
  def __init__(self, pin):
    self.pin = pin
    self.sensor = dht.DHT11(Pin(self.pin))
  
  def measure(self):
    try:
      self.sensor.measure()
      self.temperature = self.sensor.temperature()
      self.humidity = self.sensor.humidity()
    except OSError as e:
      print('Failed to read sensor.')
  
  def get_temperature(self):
    return self.temperature
  
  def get_humidity(self):
    return self.humidity