import network
from umqtt.simple import MQTTClient



# WiFi Credentials 
WiFi_SSID = "OnePlus 6"
WiFi_PASS = "Frisbae123"


# Function to connect to local WiFi
def do_wifi_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(WiFi_SSID, WiFi_PASS)
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())

