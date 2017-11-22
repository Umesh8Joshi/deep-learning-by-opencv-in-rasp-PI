"""
	dust sensing by using grove dust sensor in rapsberry pi
	by using grovepi (open source) library.
"""

#!/usr/bin/env python3

"""
	Connect dust sensor to port D2 or GIOP2 on raspberry pi.
	Sensor takes 30 seconds to update new values
"""

import time
import grovpi
import atexit

atexit.register(grovepi.dust_sensor_dis)

print("Reading from dust sensor")
grovepi.dust_sensor_en()
while True:
	try:
		[new_val,lowpulseoccupancy] = grovepi.dustSensorRead()
		if new_val:
			print(lowpulseoccupancy)
		time.sleep(5)
	except IOError:
		print("Error")