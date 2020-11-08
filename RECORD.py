# Import LocoDrone Python Module
import LocoDrone
import time
import csv

# Define USB Port Address
usb_port_address = "COM4"

a_file = open("coordinate.csv", "w")
writer = csv.writer(a_file)

# Function Called Main
def main():

	# Create Instance of LocoDrone Class to Allow Use of Loco Drone Functions
    loco_drone = LocoDrone.LocoDrone()

	# Create Connection Between Python and Controller and Start Bind-to-Drone
    loco_drone.connect(usb_port_address)

	# Set Control Mode Type for Controller Behavior
    loco_drone.set_mode(loco_drone.MODE_ACCELEROMETER)

	# Calibrate Controller Sensors
    loco_drone.controller_calibrate()

	# Calibrate Drone
    loco_drone.drone_calibrate()

	# Drone Take-off
    loco_drone.drone_takeoff()
    droop = {
            "roll: " : loco_drone.roll,
            "pitch: " : loco_drone.pitch,
            "throttle: " : loco_drone.throttle
            }
    
	# Run For 10 Seconds
    time_start = time.time()
    while ((time.time() - time_start) < 10):
        loco_drone.read_data(loco_drone.DRONE_DATA)
        loco_drone.read_data(loco_drone.ACCELEROMETER)
        loco_drone.read_data(loco_drone.GYROSCOPE)
        droop["roll: "] = loco_drone.roll
        droop["pitch: "] = loco_drone.pitch
        droop["throttle: "] = loco_drone.throttle
        for key, value in droop.items():
            writer.writerow([key, value])
            a_file.close
        
		# Short Delay of 1 Millisecond Between Iterations
        time.sleep(0.001)

	# Drone Land
    loco_drone.drone_land()

# Check if this sketch is executing as the main
if __name__ == "__main__":

	# Try to call main function
    try:
        main()
	# Break out of logic if keyboard interrupt
    except KeyboardInterrupt:
        raise