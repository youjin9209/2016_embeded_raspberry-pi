import smbus
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led_pin1 = 14
led_pin2 = 15

GPIO.setup(led_pin1, GPIO.OUT)
GPIO.setup(led_pin2, GPIO.OUT)

bus = smbus.SMBus(1)
addr = 0x23
reset = 0x27
con_hr_mode = 0x10

data1 = 0
data2 = 0
val = 0
light_val = 0

try:
    bus.write_byte(addr, reset)
    time.sleep(0.05)

    while True:
        bus.write_byte(addr, con_hr_mode)
        time.sleep(0.26)

        data1 = bus.read_byte(addr)
        data2 = bus.read_byte(addr)

        val = (data1 << 8) | data2
        light_val = val / 1.2

        print 'light_val = 5.2f' % light_val
        time.sleep(1)

        if(light_val < 300):
            GPIO.output(led_pin1, True)
            GPIO.output(led_pin2, True)
        else:
            GPIO.output(led_pin1, False)
            GPIO.output(led_pin2, False)
except:
    pass
            
            
