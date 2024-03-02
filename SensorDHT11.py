import Adafruit_DHT
import json


class SensorDHT11:
    def __init__(self, pin, name:str = "DHT11"):
        self.name = name
        self.sensor = Adafruit_DHT.DHT11
        self.pin = pin

    def read(self):
        humidity, temperature = Adafruit_DHT.read(self.sensor, self.pin)
        if humidity is not None and temperature is not None:
            logger.info("Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity))
        else:
            logger.error("Sensor failure. Check wiring.")
            return None
        return dict(humidity=humidity, temperature=temperature)

def read_sensor():

  dht11 = SensorDHT11(pin=18)
  dht11.read()


if __name__ == "__main__":
    read_sensor()
