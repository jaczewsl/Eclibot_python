import RPi.GPIO as GPIO                             # Importing RPi library to use the GPIO pins


class Rgb(object):
    def __init__(self, redPin, greenPin, bluePin):  # Three pin number arguments required
        self.redPin = redPin                        # Red pin assignment
        self.greenPin = greenPin                    # Green pin assignment
        self.bluePin = bluePin                      # Blue pin assignment
        self.MIN = 0                                # RGB(100, 0, 0) = Red | RGB(0,100,0) = Green
        self.MAX = 100                              # RGB(0, 0, 100) = Blue
        self.frequency = 100                        # Maximum brightness

        GPIO.setmode(GPIO.BCM)                      # Referring to the pins by the "Broadcom SOC channel" number
        GPIO.setwarnings(False)                     # Disable warnings
        GPIO.setup(self.redPin, GPIO.OUT)           # Setup GPIO redPin number to OUT
        GPIO.setup(self.greenPin, GPIO.OUT)         # Setup GPIO greenPin number to OUT
        GPIO.setup(self.bluePin, GPIO.OUT)          # Setup GPIO bluePin number to OUT

        self.RED = GPIO.PWM(self.redPin, self.frequency)      # Created a PWM object assigned to red pin with 100 freq
        self.GREEN = GPIO.PWM(self.greenPin, self.frequency)  # Created a PWM object assigned to green pin with 100 freq
        self.BLUE = GPIO.PWM(self.bluePin, self.frequency)    # Created a PWM object assigned to blue pin with 100 freq

        self.RED.start(self.MIN)                    # Started PWM for Red at 0% duty cycle
        self.GREEN.start(self.MIN)                  # Started PWM for Green at 0% duty cycle
        self.BLUE.start(self.MIN)                   # Started PWM for Blue at 0% duty cycle

    def redColour(self):                            # Turns on the Red Colour
        self.RED.ChangeDutyCycle(self.MAX)          # Changes duty cycle to MAX = 100
        self.GREEN.ChangeDutyCycle(self.MIN)
        self.BLUE.ChangeDutyCycle(self.MIN)

    def greenColour(self):                          # Turns on the Green Colour
        self.RED.ChangeDutyCycle(self.MIN)
        self.GREEN.ChangeDutyCycle(self.MAX)
        self.BLUE.ChangeDutyCycle(self.MIN)

    def blueColour(self):                           # Turns on the Blue Colour
        self.RED.ChangeDutyCycle(self.MIN)
        self.GREEN.ChangeDutyCycle(self.MIN)
        self.BLUE.ChangeDutyCycle(self.MAX)

    def noColour(self):                             # All pins duty cycle is set to 0
        self.RED.ChangeDutyCycle(self.MIN)
        self.GREEN.ChangeDutyCycle(self.MIN)
        self.BLUE.ChangeDutyCycle(self.MIN)

    def stopLED(self):                              # stops the PWMs
        self.RED.stop()
        self.GREEN.stop()
        self.BLUE.stop()
