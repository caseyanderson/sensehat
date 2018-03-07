#!/usr/bin/python3

'''
detect SenseHat joystick position
'''

from sense_hat import SenseHat
from time import sleep
sense = SenseHat()

blue = (0, 0, 255)
red = (255, 0, 0)

try:
    while True:
        for event in sense.stick.get_events():
            if event.action == 'pressed':
                print(event.direction, event.action)
                sense.show_message(str(event.direction), scroll_speed = 0.1, text_colour = blue, back_colour = red)
            sleep(0.05)
except KeyboardInterrupt:
    print("INTERRUPTED!")
    print("exiting")
