import RPi.GPIO as GPIO
import time

""" Definitions """

freq = 1000
pin = 18
min = 1
max = 99

""" GPIO SETTINGS """
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
pwm = GPIO.PWM(pin, freq)

""" STARTING ROUTINE """

pwm.start(0)

""" DIMMING UP """
for i in range(1,99): 
	pwm.ChangeDutyCycle(i)
	time.sleep(0.1)

""" DIMMING DOWN """
for i in range(1,99): 
	value = 100 - i
	pwm.ChangeDutyCycle(value)
	time.sleep(0.1)

""" FLASHING BOLTS """
for i in range (0, 3):
	pwm.ChangeDutyCycle(99)
	time.sleep(0.05)
	pwm.ChangeDutyCycle(1)
	time.sleep(0.05)
	pwm.ChangeDutyCycle(99)
	time.sleep(0.05)
	pwm.ChangeDutyCycle(1)
	time.sleep(3)

""" ENDING """

pwm.stop()

GPIO.cleanup()

""" EXITING """
print("Thankyou for using!\n")
