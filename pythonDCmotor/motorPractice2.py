import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO_RP = 24
GPIO_RN = 25
GPIO_EN = 12

GPIO.setup(GPIO_RP, GPIO.OUT)
GPIO.setup(GPIO_RN, GPIO.OUT)
GPIO.setup(GPIO_EN, GPIO.OUT)
p = GPIO.PWM(GPIO_RP, 100)
p.start(0)
cnt = 0

try:
	while True:
		p.ChangeDutyCycle(10)
		GPIO.output(GPIO_RN, False)
		GPIO.output(GPIO_EN, True)
		print 'angle 10'
		time.sleep(3)
		
		p.ChangeDutyCycle(35)
		GPIO.output(GPIO_RN, False)
		GPIO.output(GPIO_EN, True)
		print 'angle 35'
		time.sleep(3)
			
		p.ChangeDutyCycle(80)
		GPIO.output(GPIO_RN, False)
		GPIO.output(GPIO_EN, True)
		print 'angle 80'
		time.sleep(3)

		print 'stop'
		GPIO.output(GPIO_EN, False)
		time.sleep(3)
except KeyboardInterrupt:
	p.stop()
finally:
	GPIO.cleanup()



