import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
#GPIO.setup(7, GPIO.OUT)


def blink(numTimes, speed):
	GPIO.setup(7, GPIO.OUT)
	
	for i in range(0, numTimes):
		print "Iteration" + str(i+1)
		GPIO.output(7, True)
		time.sleep(speed)
		GPIO.output(7, False)
		time.sleep(speed)
		print "Done!"
	GPIO.cleanup()

iterations = raw_input("Enter total number of times to blink: ")
speed = raw_input("Enter length of each blink(seconds):")
blink(int(iterations), float(speed))
