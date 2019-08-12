import sys                                      # Imports sys modules
import Adafruit_DHT                             # Imports Adafruit DHT library needed for temperature reading


class Temperature(object):
    def __init__(self, sensorNo, sensorPin):
        self.humidity = 0                       # Set initial temperature to 0
        self.temperature = 0                    # Set initial humidity to 0
        self.sensorNo = sensorNo                # As DHT11 sensor is used, sensorNo will be set to 11
        self.sensorPin = sensorPin              # Sensor pin assignment

        self.calculate()                        # Call function during creation

    def calculate(self):                        # Read from sensor and assigns values for temperature and humidity
        self.humidity, self.temperature = Adafruit_DHT.read_retry(self.sensorNo, self.sensorPin)

        if self.temperature is not None and self.humidity is not None:
            print 'Temp: {0:0.1f}*C  Humidity: {1:0.1f}%'.format(self.temperature, self.humidity)
        else:
            print "Can't read from sensor!"

    def getTemperature(self):                   # Returns temperature value
        return self.temperature

    def getHumidity(self):                      # Returns humidity value
        return self.humidity
