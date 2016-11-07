import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
gpio_pin = 13
scale = [1046, 1174, 1318, 1396, 1567,1760, 1975, 2093]
GPIO.setup(gpio_pin, GPIO.OUT)

try:
	p = GPIO.PWM(gpio_pin, 100)
	p.start(100)
	p.ChangeDutyCycle(90)

	for i in range(8):
		print (i+1)
		p.ChangeFrequency(scale[i])
		time.sleep(1)
	p.stop()

finally:
	GPIO.setup()
