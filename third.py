#!/usr/bin/env python3
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.sound import Sound
from time import sleep
from threading import Thread

ts = TouchSensor()
sound = Sound()

def twenty_tones():
    for j in range(0,20):           # Do twenty times.
        sound.play_tone(1000, 0.2)  # 1000Hz for 0.2s
        sleep(0.5)

t = Thread(target=twenty_tones)
t.start()

for i in range(0,5):       # Do five times, with i = 0, 1, 2, 3, 4.
    ts.wait_for_bump()

sound.beep()

