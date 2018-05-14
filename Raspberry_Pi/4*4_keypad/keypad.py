#--------------------------------------
#Program for 4*4 Keypad
#
#
#Author : Lal Bosco Lawrence
#Date   : 28-April-2018
#--------------------------------------

#import
import RPi.GPIO as GPIO
import time

GPIO.setmode (GPIO.BOARD)

######### Keypad Initialization ################
MATRIX = [ [1  , 2, 3  , 'A'],
           [4  , 5, 6  , 'B'],
           [7  , 8, 9  , 'C'],
           ['*', 0, '#', 'D']
         ]

ROW =   [7 ,11,13,15]  #keypad_pin (0-3)
COL =   [12,16,18,22]  #keypad_pin (4-7)
#################################################

#Row pin initialization as output
for j in range(4):
	GPIO.setup(COL[j], GPIO.OUT)
	GPIO.output(COL[j], 1)

#Column polumnin initialization as input
for i in range (4):
	GPIO.setup(ROW[i], GPIO.IN, pull_up_down = GPIO.PUD_UP)

#Run a loop to read keypad
while(True):
	for j in range (4):
		GPIO.output(COL[j],0)

		for i in range(4):
			if GPIO.input (ROW[i]) == 0:
				print MATRIX[i][j]
				time.sleep(0.5)
				while (GPIO.input(ROW[i]) == 0):
					pass

		GPIO.output(COL[j],1)

