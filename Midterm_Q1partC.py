# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 14:52:46 2020

@author: jelya
"""

import LocoDrone
import time

usb_port_address1 = "COM3"
#usb_port_address2 = "COM5"

def trim_print(drone_object):
	print("Pitch_Trim: " + str(drone_object.pitch_trim) + "    " +
		    "Roll_Trim: " + str(drone_object.roll_trim))

def trim_set(drone_object, roll_val, pitch_val):
	# Update Drone With New Data When Key Pressed
	drone_object.pitch_trim = pitch_val
	drone_object.roll_trim = roll_val
	drone_object.set_data(0, 0, 0) # Update Drone With New Trim Data

def main():
    loco_drone = LocoDrone.LocoDrone()
    
#    loco_drone_JR = LocoDrone.LocoDrone()
    
    loco_drone.connect(usb_port_address1)
    
#    loco_drone_JR.connect(usb_port_address2)
    
    loco_drone.set_mode(loco_drone.MODE_CONTROL)
    
#    loco_drone_JR.set_mode(loco_drone.MODE_CONTROL)
    
    loco_drone.controller_calibrate()
    
#    loco_drone_JR.controller_calibrate()
    
    loco_drone.drone_calibrate()
    
#    loco_drone_JR.drone_calibrate()
    
    loco_drone.drone_takeoff()
    
#    loco_drone_JR.drone_takeoff()
    
    time.sleep(1)
    
#    loco_drone.trim_orientation()
#    trim_print(loco_drone)
    
    # Uncomment and use this to set the trim value directly once it is known    
    trim_set(loco_drone, -5, -5.5)
    
#    trim_set(loco_drone_JR, -2, -1)
    #charlie -6 -6
    #charlie jr -2 -1
    
    loco_drone.set_data(0, 0, 0)
    time.sleep(1)
    
#    loco_drone_JR.set_data(0, 0, 0)
#    time.sleep(2)
   
    loco_drone.set_data(0, 20, 0)
    time.sleep(3)
    
#    loco_drone_JR.set_data(-15, 0, 0)
#    time.sleep(3)
    
    loco_drone.set_data(20, 10, 0)
    time.sleep(3)
    
##    loco_drone_JR.set_data(10, -5, 0)
##    time.sleep(3)
    


    loco_drone.set_data(20, -5, 0)
    time.sleep(3)
    
##    loco_drone_JR.set_data(-10, -5, 0)
##    time.sleep(3)

    loco_drone.set_data(-9, -4, 0)
    time.sleep(3)
    
#    loco_drone_JR.set_data(-10, 5, 0)
#    time.sleep(3)

    loco_drone.drone_land()
    
#    loco_drone_JR.drone_land()
    
    
if __name__ == "__main__":

	# Try to call main function
	try:
		main()
	# Break out of logic if keyboard interrupt
	except KeyboardInterrupt:
		raise



time