import time
import machine
from wifi_connection import do_wifi_connect

do_wifi_connect()

led = machine.Pin(2, machine.Pin.OUT)

for i in range(3):
    led.value(0)
    time.sleep(0.5)
    led.value(1)
    time.sleep(0.5)

import hcsr04

ultrasonic = hcsr04.HCSR04(trigger_pin=13, echo_pin=12, echo_timeout_us=1000000)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  dataLoggerTS.py
#  
#  Copyright 2018 Marcelo Rovai 
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

# import general libraries
from umqtt.simple import MQTTClient

# ThingSpeak Credentials:
SERVER = "mqtt.thingspeak.com"
CHANNEL_ID = "1672220"
WRITE_API_KEY = "27HADYNIQBN4ZSMW"
PUB_TIME_SEC = 30

# MQTT client object
client = MQTTClient("umqtt_client", SERVER)

# Create the MQTT topic string
topic = "channels/" + CHANNEL_ID + "/publish/" + WRITE_API_KEY



while True:
    distance = ultrasonic.distance_cm()
    print('Distance:', distance, 'cm', '|', distance/2.54, 'inch')
    payload = "field1="+'Distance:' + str(distance) + 'cm' + '|' + str(distance/2.54) + 'inch'
    client.connect()
    client.publish(topic, payload)
    client.disconnect()
    if distance <= 10:
        led.value(1)
    else:
        led.value(0)
    time.sleep_ms(1000)