# Program to using switch on RPi3.
# Author : Lal Bosco Lawrence
# Date   : 30/12/2017

import RPi.GPIO as GPIO          #Import GPIO library
import time                      #Import time library
GPIO.setmode(GPIO.BOARD)         #Set GPIO pin numbering

SWITCH_PIN = 12      # Switch pin
TIME_DELAY = 0.3     # Delay in sec

GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Enable input and pull up resistors

while True:
        input_state = GPIO.input(SWITCH_PIN) #Read and store value of input to a variable
        if input_state == True:     #Check whether button is pressed
            print('Button is Pressed...')   #Print 'Button Pressed'
            time.sleep(TIME_DELAY)           #Delay of 0.3s
