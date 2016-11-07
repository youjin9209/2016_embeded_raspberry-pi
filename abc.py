import Tkinter as tk
import time

def handle_key(event):
	key = event.char
	if key == 'a':
		print "a"
	elif key == 's':
		print "s"

root = tk.Tk()
root.bind_all('<Key>', handle_key)
root.withdraw()
root.mainloop()
