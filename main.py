import logging
import sys
import time
from sensing import *

sensingObject=sensingClass() # global sensing class object creation

class Main_class(): # Main class creation to start the flow
    
    def CoilOS_init(self): # function to call sensing and initiate the coilOS flow
        global sensingObject
        print("In the CoilOS_init of the main class")
        sensingObject.sensing_initializer() # sensing class function has been called
        print("Out of the sensing call")
        
    def main():
        print("In the main class")
    
if __name__ == "__main__": # main function to call fucntions of the class
    instance=Main_class()
    instance.CoilOS_init()
    