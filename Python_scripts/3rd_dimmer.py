from gpiozero import PWMLED
import time

""" Definitions """

freq = 100
pin = 18
min = 0
max = 100

""" GPIO SETTINGS """
pwm = PWMLED(pin)

""" STARTING ROUTINE """


check = 0
while (check == 0):
	value = input("Enter value for dimmer\n range 1 - 99: (-1 to end)\n")
	if (value == -1):
		pwm.value = 1
		check = -1
	elif (value <= min) or (value >=  max):
		print("Out of range! Acceptable values only in 1-99\n")
	else:
		print (value)
		pwm.value = value
		time.sleep(1) 



""" EXITING """
print("Thankyou for using!\n")
