import RPi.GPIO as GPIO                             # Importing RPi library to use the GPIO pins
from time import sleep                              # Sleep function used for 'breaking' the signal


class Buzzer(object):
    def __init__(self, buzzer_pin):                 # Pin number required when creating an instance of the class
        self.buzzer_pin = buzzer_pin                # Buzzer pin assignment
        GPIO.setmode(GPIO.BCM)                      # Referring to the pins by the "Broadcom SOC channel" number
        GPIO.setwarnings(False)                     # Disable warnings
        GPIO.setup(buzzer_pin, GPIO.OUT)            # Setup GPIO buzzer_pin number to OUT

    def buzzOn(self):                               # Turns buzzer on
        try:
            GPIO.output(self.buzzer_pin, True)

        except KeyboardInterrupt:
            print "CTRL + C was pressed"
            GPIO.cleanup()                          # Make all the output pins LOW
            print "GPIO.cleanup() done"

    def buzzOff(self):                              # Turns buzzer off
        try:
            GPIO.output(self.buzzer_pin, False)

        except KeyboardInterrupt:
            print "CTRL + C was pressed"
            GPIO.cleanup()                          # Make all the output pins LOW
            print "GPIO.cleanup() done"

    def buzzForSec(self, time):                     # Turns buzzer on for specified amount of time
        self.buzzOn()
        sleep(time)
        self.buzzOff()
