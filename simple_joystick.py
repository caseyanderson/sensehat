#!/usr/bin/python3

'''
detect SenseHat joystick position
'''

from sense_hat import SenseHat
from time import sleep
sense = SenseHat()

blue = (0, 0, 255)
green = (0, 255, 0)

try:
    while True:
        for event in sense.stick.get_events():
            if event.action == 'pressed':
                print(event.direction, event.action)
                msg = str(event.direction)  # just the direction
#                msg = ''.join([event.direction, ' ', event.action])
                sense.show_message(msg, scroll_speed = 0.05, text_colour = blue, back_colour = green)
            sleep(0.05)
except KeyboardInterrupt:
    print("INTERRUPTED!")
    print("exiting")
    sense.clear()
