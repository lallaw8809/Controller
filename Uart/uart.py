# Program to uart communication.
# Author : Lal Bosco Lawrence
# Date   : 31/12/2017

import serial

#Uart configuration with baud rate
port = serial.Serial("/dev/ttyS0", baudrate=115200, timeout=3.0)

port.write("\nUART Communication...\n")

while True:
    rcv = port.read(1) #Receive the data from terminal
    port.write((rcv))  #Transfer the received data into terminal


