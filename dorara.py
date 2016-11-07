import RPi.GPIO as GPIO
import time
import curses

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
gpio_pin = 13
GPIO.setup(gpio_pin, GPIO.OUT)

p = GPIO.PWM(gpio_pin, 100)
GPIO.output(gpio_pin, True)
p.start(100)
p.ChangeDutyCycle(90)

scaleOfkey = {'a': 261, 's': 264, 'd': 329, 'f': 349, 'g': 392, 'h': 440, 'j': 493, 'k': 523}

stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(1)

stdscr.addstr(0, 10, "Hit 'q' to quit")
stdscr.nodelay(1)
Richtung = ''

while Richtung != ord('q'):
	stdscr.refresh()
	Richtung = stdscr.getch()
	stdscr.addch(20, 25, Richtung)

	if Richtung == ord('a'):
		p.ChangeFrequency(scaleOfkey['a'])
		time.sleep(1)
	
	elif Richtung == ord('s'):
		p.ChangeFrequency(scaleOfkey['s'])
		time.sleep(1)

curses.nocbreak()
stdscr.keypad(0)
curses.endwin()  
