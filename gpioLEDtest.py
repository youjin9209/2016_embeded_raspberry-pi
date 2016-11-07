import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
led_pin1 = 14
GPIO.setup(led_pin1, GPIO.OUT)

def blink(num):
	t = 1
	for i in range(0, num):
		GPIO.output(led_pin1, True)
		time.sleep(t)
		GPIO.output(led_pin1, False)
		time.sleep(t)
		t = t + 1
	print "I am done"
	GPIO.clenup()

if __name__ == "__main__":
	n = int(input("Put a number : "))
	blink(n)
		
