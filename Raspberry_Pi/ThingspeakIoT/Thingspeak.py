#---------------------------------------------------
# Program to get the sensor data (IR and Vibration)
# and update into cloud at regular intervals.
#
# Author : Lal Bosco
# Date   : 14-May-2018
#---------------------------------------------------

#!/usr/bin/env python

import httplib, urllib
import RPi.GPIO as GPIO
import time
import threading

#Sensor's pin
IR_SENSOR  = 3
VIBRATION  = 5

ir_value = 0
vibration_value = 0;

thread = []

sleep = 16 # how many seconds to sleep between posts to the channel
key = 'XXXXXXXXXXXX'  # Thingspeak channel API Key

#Report sensor data (IR and vibration) to Thingspeak Channel
def sensor_data_update():
    global ir_value ,vibration_value
    while True:
        #Upload sensor datails into cloud
        params = urllib.urlencode({'field1': ir_value, 'field2': vibration_value, 'key':key }) 
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = httplib.HTTPConnection("api.thingspeak.com:80")
        #Reset the sensor values
        vibration_value = 0
	ir_value        = 0
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            data = response.read()
            conn.close()
        except:
            print "connection failed"
        break

#Validation of sensor data
def polling_sensor_data():
	global ir_value ,vibration_value
	
	#Read the sensors value
	while 1:
		if(GPIO.input(IR_SENSOR) == 1):
			ir_value = 1
	
	        if(GPIO.input(VIBRATION) == 1):
			vibration_value =1
	return;

def main():
	global ir_value ,vibration_value
	#Sensor's pin initialization as a output
	GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(IR_SENSOR,GPIO.IN,pull_up_down = GPIO.PUD_UP)
        GPIO.setup(VIBRATION,GPIO.IN,pull_up_down = GPIO.PUD_UP)

        #creation of thread to polling the sensor data
	t = threading.Thread(target=polling_sensor_data)
        #Starts the thread
	t.start()
	
	while True:
		print 'Sensor status ', ir_value,vibration_value
		#Update the sensor data into cloud at regular interval
		sensor_data_update() 
		time.sleep(sleep)

if __name__ == '__main__':
	main()

