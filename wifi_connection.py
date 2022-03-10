import network
from umqtt.simple import MQTTClient

# ThingSpeak Credentials:
SERVER = ""
CHANNEL_ID = ""
WRITE_API_KEY = ""
PUB_TIME_SEC = 30

# MQTT client object
client = MQTTClient("umqtt_client", SERVER)

# Create the MQTT topic string
topic = "channels/" + CHANNEL_ID + "/publish/" + WRITE_API_KEY

# WiFi Credentials 
WiFi_SSID = "OnePlus 6"
WiFi_PASS = "Frisbae123"


# Function to connect to local WiFi
def do_wifi_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(WiFi_SSID, WiFi_SSID)
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())

