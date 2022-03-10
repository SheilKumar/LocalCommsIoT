import time
import machine

led = machine.Pin(2, machine.Pin.OUT)

for i in range(10):
    led.value(0)
    time.sleep(0.5)
    led.value(1)
    time.sleep(0.5)

import hcsr04

ultrasonic = hcsr04.HCSR04(trigger_pin=13, echo_pin=12, echo_timeout_us=1000000)


while True:
    distance = ultrasonic.distance_cm()
    print('Distance:', distance, 'cm', '|', distance/2.54, 'inch')
    if distance <= 10:
        led.value(1)
    else:
        led.value(0)
    time.sleep_ms(1000)