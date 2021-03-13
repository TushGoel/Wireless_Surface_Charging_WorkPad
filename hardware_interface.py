import serial
import RPi.GPIO as GPIO
import time
import re
import logging
import sys

class hardware_interface():

    def __init__(self):
        print("At the start of init of hardware")
        self.serial_connection_0 = None
        self.serial_connection_1=None
        print("Before the try block")
        
        try:
            print("In the beginning of the try block")
            logging.info('Creating serial connection with serial device')
           
            # Sensing
            self.serial_connection_0 = serial.Serial("/dev/ttyACM0", 9600) #Establishing serial communication connection between arduino and raspberry pi
            self.serial_connection_0.baudrate = 9600 #Initializing the baudrate for comuunication
            
            print("In the end of the try block before time sleep")
            time.sleep(3) #As per politeness, for establishing connection between arduino and Raspberry Pi
            print("In the end of the it doesnt even matter")
            
        except Exception as e:
            logging.error(e)
            logging.error("Couldnt create object and read from serial device")
            sys.exit(0)

        print("Completed the __init__ of hardware_interface \n")
        
    def initSerialComm_0(self):
        return self.serial_connection_0 #returning the serial connection established for interfacing between arduino and raspberry pi
    
    def initSerialComm_1(self):
        return self.serial_connection_1 #returning the serial connection established for interfacing between arduino and raspberry pi

    def pinsManagement(self,pin,pin_state): #writing the data to the arduino for turning the pin on and off according to the instruction received
        print("In the pins Management")
        print(pin)
        print(pin_state)
        send_data=pin + ',' + pin_state
        print(send_data)
        data=send_data.encode() #converting the data into arduino readable format before transmitting it to arduino for completing the functionality
        print(data)
        self.serial_connection_1.write(data)
        print("Out of it")
      