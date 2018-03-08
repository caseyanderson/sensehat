#!/usr/bin/python3

'''
detect SenseHat joystick position and action
'''

from sense_hat import SenseHat
from time import sleep
sense = SenseHat()

blue = (0, 0, 255)
green = (0, 255, 0)

try:
    while True:
        for event in sense.stick.get_events():
            print(event.direction, event.action)
            msg = ''.join([str(event.direction), ' ', str(event.action)])  # just the direction
            sense.show_message(msg, scroll_speed = 0.085, text_colour = blue, back_colour = green)
        sleep(0.1)
except KeyboardInterrupt:
    print("INTERRUPTED!")
    print("exiting")
    sense.clear()
