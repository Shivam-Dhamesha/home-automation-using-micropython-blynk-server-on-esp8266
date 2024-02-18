# Import required modules
import network # To connect to a network 
from machine import Pin # To access harware
import blynklib # Library for interfacing harware with Blynk IOT platform


# Connect to Wi-Fi network


wifi_ssid = "BRAIN" # WIFI used to connect to internet
wifi_password = "gzzu5040" # WIFI password


sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect(wifi_ssid, wifi_password)# trying to connect with given network


while not sta_if.isconnected():
    pass


print("Wi-Fi connected:", sta_if.ifconfig())


# Connect to Blynk server


auth_token = "7ogFPZIINLaiMQNftGRkKeKaG_sPTvQu" # unique auth to connect to blynk server
blynk = blynklib.Blynk(auth_token) # blynk connect


# Define GPIO pin number


relay = Pin(5, Pin.OUT)


# Define Blynk virtual pin handlers


@blynk.on("V0")
def v0_handler(value):
    if int(value[0]) == 1:
        relay.value(0) # relay used was low level trigger 0 = ON
        
    else:
        relay.value(1) # relay used was low level trigger 1 = OFF
        


# Start Blynk loop
while True:
    blynk.run()
