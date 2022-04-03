# Define either work for actuation if motor recieved
# Else simulate 

import machine

def do_actuation():
    p4 = machine.Pin(4)
    servo = machine.PWM(p4, freq=50)
    servo.duty(70)
    return