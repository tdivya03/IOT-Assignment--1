#!/usr/bin/env python3
import bluetooth
import os
import time
from sense_hat import SenseHat

# Main function
def main():
    print("Program will display the list of devices conencted to bluetooth")
    search()

# Search for device based on device's name
def search():
    while True:
        dt = time.strftime("%a, %d %b %y %H:%M:%S", time.localtime())
        print("\nCurrently: {}".format(dt))
        time.sleep(3) #Sleep three seconds 
        nearby_devices = bluetooth.discover_devices()

        for mac_address in nearby_devices:
		    #device_name = bluetooth.lookup_name(mac_address)
            print("MAC address: {}".format(mac_address))
			sense = SenseHat()
            temp = round(sense.get_temperature(), 1)
            sense.show_message("Thanks for connecting to Raspberry , your Mac address is {}! and Current Temp is {}*c".format(mac_address,temp), scroll_speed=0.05)
        

#Execute program
main()