import RPi.GPIO as GPIO
import time

""" Definitions """

freq = 100
pin = 18
min = 0
max = 99

""" GPIO SETTINGS """
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
pwm = GPIO.PWM(pin, freq)

""" STARTING ROUTINE """

pwm.start(0)

check = 0
while (check == 0):
	value = input("Enter value for dimmer\n range 1 - 99: (-1 to end)\n")
	if (value == -1):
		pwm.ChangeDutyCycle(1)
		check = -1
	elif (value <= min) or (value >=  max):
		print("Out of range! Acceptable values only in 1-99\n")
	else:
		print (value)
		pwm.ChangeDutyCycle(value)
		time.sleep(1) 

pwm.stop()

GPIO.cleanup()

""" EXITING """
print("Thankyou for using!\n")
