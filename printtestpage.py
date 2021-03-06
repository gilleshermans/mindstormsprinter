#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
from threading import Thread

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

# lettergroottes instellen
def l1(seg1):
    return seg1 * 1

def l2(seg1):
    return seg1 * 2

def l3(seg1):
    return seg1 * 3

def l4(seg1):
    return seg1 * 4

# INITAILISERING
brick.light(Color.RED)
lijn_pos = 525
lijn_breedte = 1050
letterspatie = 20
l1(10)
l2(10)
l3(10)
l4(10)
Qpos = 0
queue = []
EStop = False
penM = Motor(Port.C)
lijnM = Motor(Port.A)

# lijnbeweging

def lijnbeweging(b):
    lijnM.run_angle(500, b-lijn_pos)
    global lijn_posL
    lijn_posL = b
    return lijn_posL
    if b == 0:
        lijnM.run_angle(-200, 10)
        lijnM.run_angle(200, 10)