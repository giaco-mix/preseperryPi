import wiringpi as piwiring
import time

""" Definitions """

freq = 100
pin2 = 18
min = 0
max = 1024

""" GPIO SETTINGS """
piwiring.wiringPiSetupGpio()
piwiring.pinMode(pin2, 2)

""" STARTING ROUTINE """
piwiring.pwmWrite(pin2, 0)

check = 0
while (check == 0):
	value = input("Enter value for dimmer\n range 0 - 1024: (-1 to end)\n")
	if (value == -1):
		piwiring.pwmWrite(pin2, 0)
		check = -1
	elif (value < min) or (value >  max):
		print("Out of range! Acceptable values only in 1-99\n")
	else:
		print (value)
		piwiring.pwmWrite(pin2, value)
		time.sleep(1) 



""" EXITING """
print("Thankyou for using!\n")
