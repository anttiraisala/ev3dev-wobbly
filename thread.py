#!/usr/bin/env python3

from time import sleep

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds
from ev3dev2.sound import Sound

sound = Sound()
sound.speak('Welcome to the E V 3 dev project!')

sound.play_song((
    ('D4', 'e3'),
    ('D4', 'e3'),
    ('D4', 'e3'),
    ('G4', 'h'),
    ('D5', 'h')
))

import os
os.system('setfont Lat15-TerminusBold14')
print('EV3 Python rules!')




# TODO: Add code here

ts = TouchSensor()
leds = Leds()

print("Press the touch sensor to change the LED color!")

from threading import Thread


def task():

    while True:
        if ts.is_pressed:
            leds.set_color("LEFT", "GREEN")
            leds.set_color("RIGHT", "GREEN")
        else:
            leds.set_color("LEFT", "RED")
            leds.set_color("RIGHT", "RED")
        # don't let this loop use 100% CPU
        sleep(0.01)


t1 = Thread(target=task)
t1.start()


m = LargeMotor(OUTPUT_A)
m.on_for_rotations(SpeedPercent(75), 5)




while True:
    sleep(0.01)

