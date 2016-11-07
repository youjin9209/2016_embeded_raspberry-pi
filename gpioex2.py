import RPi.GPIO as GPIO
import time

led_pin1 = 14
led_pin2 = 15

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin1, GPIO.OUT)
GPIO.setup(led_pin2, GPIO.OUT)

def blink():
	print("Starting blinking fever!")
	iteracion = 0
	while iteracion < 30:
		GPIO.output(led_pin1, True)
		GPIO.output(led_pin2, False)
		time.sleep(1)
		GPIO.output(led_pin1, False)
		GPIO.output(led_pin2, True)
		time.sleep(1)
		iteracion = iteracion + 2
	print("I'm done!")
	GPIO.cleanup()
blink()
