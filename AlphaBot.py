import RPi.GPIO as GPIO							# Importing RPi library to use the GPIO pins


class AlphaBot(object):
	def __init__(self, in1=12, in2=13, ena=6, in3=20, in4=21, enb=26):  # Theses pins are set according to manufacturer
		self.IN1 = in1  						# Left motor
		self.IN2 = in2  						# Left motor
		self.IN3 = in3  						# Right motor
		self.IN4 = in4  						# Right motor
		self.ENA = ena  						# When HIGH is set, the PWM pulse will be outputted from IN1,
		self.ENB = enb  						# IN2, IN3 and IN4 so as to control the speed of the motor

		GPIO.setmode(GPIO.BCM)					# Referring to the pins by the "Broadcom SOC channel" number
		GPIO.setwarnings(False)					# Disable warnings
		GPIO.setup(self.IN1, GPIO.OUT)  		# Setup GPIO pin12 to OUT
		GPIO.setup(self.IN2, GPIO.OUT)  		# Setup GPIO pin13 to OUT
		GPIO.setup(self.IN3, GPIO.OUT)  		# Setup GPIO pin20 to OUT
		GPIO.setup(self.IN4, GPIO.OUT)  		# Setup GPIO pin21 to OUT
		GPIO.setup(self.ENA, GPIO.OUT)  		# Setup GPIO pin6 to OUT
		GPIO.setup(self.ENB, GPIO.OUT)  		# Setup GPIO pin26 to OUT

		self.PWMA = GPIO.PWM(self.ENA, 500)		# Create PWM instance with frequency
		self.PWMB = GPIO.PWM(self.ENB, 500)

	def forward(self):							# AlphaBot moves forward until stopped
		GPIO.output(self.IN1, GPIO.HIGH)
		GPIO.output(self.IN2, GPIO.LOW)
		GPIO.output(self.IN3, GPIO.LOW)
		GPIO.output(self.IN4, GPIO.HIGH)

	def stop(self):								# AlphaBot stops
		GPIO.output(self.IN1, GPIO.LOW)
		GPIO.output(self.IN2, GPIO.LOW)
		GPIO.output(self.IN3, GPIO.LOW)
		GPIO.output(self.IN4, GPIO.LOW)

	def backward(self):							# AlphaBot moves backward until stopped
		GPIO.output(self.IN1, GPIO.LOW)
		GPIO.output(self.IN2, GPIO.HIGH)
		GPIO.output(self.IN3, GPIO.HIGH)
		GPIO.output(self.IN4, GPIO.LOW)

	def left(self):								# AlphaBot turns left | right motor rotates
		GPIO.output(self.IN1, GPIO.LOW)
		GPIO.output(self.IN2, GPIO.LOW)
		GPIO.output(self.IN3, GPIO.LOW)
		GPIO.output(self.IN4, GPIO.HIGH)

	def right(self):							# AlphaBot turns right | left motor rotates
		GPIO.output(self.IN1, GPIO.HIGH)
		GPIO.output(self.IN2, GPIO.LOW)
		GPIO.output(self.IN3, GPIO.LOW)
		GPIO.output(self.IN4, GPIO.LOW)
		
	def setPWMA(self, value):					# Changes the Duty Cycle of signal in the range 0-100
		self.PWMA.ChangeDutyCycle(value)

	def setPWMB(self, value):					# Changes the Duty Cycle of signal in the range 0-100
		self.PWMB.ChangeDutyCycle(value)	
		
	def setMotor(self, left, right):
		if((right >= 0) and (right <= 100)):
			GPIO.output(self.IN1, GPIO.HIGH)
			GPIO.output(self.IN2, GPIO.LOW)
			self.PWMA.ChangeDutyCycle(right)
		elif((right < 0) and (right >= -100)):
			GPIO.output(self.IN1, GPIO.LOW)
			GPIO.output(self.IN2, GPIO.HIGH)
			self.PWMA.ChangeDutyCycle(0 - right)
		if((left >= 0) and (left <= 100)):
			GPIO.output(self.IN3, GPIO.HIGH)
			GPIO.output(self.IN4, GPIO.LOW)
			self.PWMB.ChangeDutyCycle(left)
		elif((left < 0) and (left >= -100)):
			GPIO.output(self.IN3, GPIO.LOW)
			GPIO.output(self.IN4, GPIO.HIGH)
			self.PWMB.ChangeDutyCycle(0 - left)
