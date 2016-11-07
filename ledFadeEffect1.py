import wiringpi
import time

io = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_PINS)
io.pinMode(1, io.PWM_OUTPUT)
io.pinMode(1, io.OUTPUT)
io.pwmWrite(1,0)
io.pinMode(1,io.PWM_OUTPUT)

value = 0
increment = 4
increasing = True
wiringpi.pinMode(1,1)
count = 0
wiringpi.digitalWrite(1,1)

while count < 100000:
	wiringpi.pinMode(1,1)
	io.pwmWrite(1,value)
	
	if increasing:
		value += increment
		time.sleep(0.002)
	else:
		value -= increment
		time.sleep(0.002)
	if (value >= 1024):
		increasing = False
	if(value <= 0):
		increasing = True
	time.sleep(0.002)
	count = count + 1
