#!/usr/bin/env python3

from time import sleep, perf_counter

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds
from ev3dev2.sound import Sound
from ev3dev2.button import Button

from threading import Thread

# Import math Library
import math

sound = Sound()
sound.speak('Welcome to the E V 3 dev project!')
sound.speak('Press backbutton on brick to quit.')


def sw():
    sound.play_song((
        ('D4', 'e3'),
        ('D4', 'e3'),
        ('D4', 'e3'),
        ('G4', 'h'),
        ('D5', 'h')
    ))

tSW = Thread(target=sw)
tSW.start()

import os
os.system('setfont Lat15-TerminusBold14')
print('EV3 Python rules!')




# TODO: Add code here

ts = TouchSensor()
leds = Leds()

print("Press the touch sensor to change the LED color!")




btn = Button()
runLoop = True

def backspace(state):
    if state:
        print('Backspace button pressed')
    else:
        print('Backspace button released')
        global runLoop
        runLoop = False

btn.on_backspace=backspace

m = LargeMotor(OUTPUT_A)
mb = LargeMotor(OUTPUT_B)

def task_runMotorB():

    while runLoop:
        speeda = math.sin(perf_counter()*2.0) * 25.0
        m.on(speed=speeda)

        speedb = math.sin(perf_counter()) * 100.0
        mb.on(speed=speedb)

        # don't let this loop use 100% CPU
        sleep(0.01)


tMotorB = Thread(target=task_runMotorB)
tMotorB.start()



while runLoop:
    if ts.is_pressed:
        leds.set_color("LEFT", "GREEN")
        leds.set_color("RIGHT", "GREEN")
    else:
        leds.set_color("LEFT", "RED")
        leds.set_color("RIGHT", "RED")

    btn.process()

    # don't let this loop use 100% CPU
    sleep(0.01)


sleep(1)

m.off()
mb.off()

sound.speak('Goodbye!')
