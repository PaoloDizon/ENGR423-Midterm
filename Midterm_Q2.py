# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 15:22:31 2020

@author: paolo
"""
import LocoDrone
import time
import csv

usb_port_address1 = "COM4"
roll =[]
pitch = []
throttle = []

with open("Midtermq2csv.csv" , "r") as csvfile:
    read = csv.DictReader(csvfile, delimiter = ',')
    for line in read:
        roll.append(int(line['Roll']))
        pitch.append(int(line['Pitch']))
        throttle.append(int(line['Throttle']))
#print(roll)
#print(pitch)
#print(throttle)
        
        
def trim_print(drone_object):
	print("Pitch_Trim: " + str(drone_object.pitch_trim) + "    " +
		    "Roll_Trim: " + str(drone_object.roll_trim))

def trim_set(drone_object, roll_val, pitch_val):
	# Update Drone With New Data When Key Pressed
	drone_object.pitch_trim = pitch_val
	drone_object.roll_trim = roll_val
	drone_object.set_data(0, 0, 0) # Update Drone With New Trim Data
    
def main():
    i = 0
    loco_drone = LocoDrone.LocoDrone()
    loco_drone.connect(usb_port_address1)
    loco_drone.set_mode(loco_drone.MODE_CONTROL)
    loco_drone.controller_calibrate()
    loco_drone.drone_takeoff()
    trim_set(loco_drone, -5, -5)
    
    end = len(roll)
    
    while i < end:
        x = roll[i]
        y = pitch[i]
        z = throttle[i]
        loco_drone.set_data(x,y,z)
        time.sleep(1)
        i += 1
    loco_drone.drone_land()
    
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        raise
time