# Define either work for actuation if motor recieved
# Else simulate 
import time
import machine

def do_actuation():
    p4 = machine.Pin(4)
    servo = machine.PWM(p4, freq=1000)
    servo.duty(512)
    time.sleep_ms(5000)
    servo.freq(50)
    return