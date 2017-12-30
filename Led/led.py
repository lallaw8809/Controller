# Program to blink the LED at regular intervel.
# Author : Lal Bosco Lawrence
# Date   : 30/12/2017

import RPi.GPIO as GPIO # Import GPIO library
import time

LED_PIN    = 7 # GPIO pin Number
TIME_DELAY = 1 # Time delay in sec

GPIO.setmode(GPIO.BOARD)      # Use board pin numbering
GPIO.setup(LED_PIN, GPIO.OUT) # Setup GPIO Pin 7 to Output

# Blink the LED
while True:
    GPIO.output(LED_PIN,True)  # Turn ON GPIO pin 7
    time.sleep(TIME_DELAY)
    GPIO.output(LED_PIN,False) # Turn OFF GPIO pin 7
    time.sleep(TIME_DELAY)


