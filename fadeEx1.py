import RPi.GPIO as GPIO
import time

led_pin1 = 14
led_pin2 = 15
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin1, GPIO.OUT)
GPIO.setup(led_pin2, GPIO.OUT)
p = GPIO.PWM(led_pin1, 50)
p2 = GPIO.PWM(led_pin2, 50)

p.start(0)
#p2.start(0)

try:
	while 1:
		for dc in range(0, 101, 5):
			if dc == 100:
				p2.start(0)				
			p.ChangeDutyCycle(dc)
			p2.ChangeDutyCycle(100-dc)
			time.sleep(0.1)
		for dc in range(100, -1, -5):
			p.ChangeDutyCycle(dc)
			p2.ChangeDutyCycle(100-dc)
			time.sleep(0.1)

except KeyboardInterrupt:
	pass
p.stop()
p2.stop()
print "Program is terminated..!!!"
GPIO.cleanup()


