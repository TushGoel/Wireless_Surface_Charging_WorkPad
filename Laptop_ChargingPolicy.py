import logging
import threading
import datetime
import time
from _surface import *
import global_var
from error_detection import *
error_detectionObject=error_detection()


surfaceObject=surface()


class LaptopchargingPolicy(threading.Thread):
    ##This method initializes all the parameters required for laptop charging policy
    #@param self The object pointer
    #@param localization_data  is a array containing x, y co-ordinates and device type returned from sensing module

    localization_data=[]

    def __init__(self,locationData):
        threading.Thread.__init__(self)
        self.localization_data=locationData

    def run(self):
        global error_detectionObject
        print("sessions in progress: ",global_var.sessionInProgress) #sessions in progress
        print("data received in initCharging of LaptopchargingPolicy:",self.localization_data)
        print("in the init_charging policy")
        global surfaceObject
        device=self.localization_data[2]
        coil,region=surfaceObject.locationCoilsMapping(self.localization_data)
        print("In the Laptop Charging Policy")
        print("Coil detected: ",coil, "and region: ",region)
        surfaceObject.activateCoil(coil,device)
                
        x1 = self.checkCharging(coil,device)
        
        if x1==0:
            self.terminateCoilCharging(coil,device)
            global_var.devices.remove(device)
            error_detectionObject.charging_error(1)
            
        else:
            surfaceObject.activateCoil(coil,device)
            self.continueCharging(x1,coil,device)     
            error_detectionObject.charging_error(0)   

    ##This method checks the feedback from the charging coils continuously and exits when not charging
    #@param self The object pointer
    #@param coil Is the coil number for which the Power Management feedback is requested
    #@param device Defines the type of device for which we need the PM feedback
    def checkCharging(self,coil,device):
        print("In the check charging")
        x=1
        while x:
            x=self.readPMFeedback(coil,device)
            return x
        return 0

    ##This method reads the feedback from the charging coils and returns true when charging
    #@param self The object pointer
    #@param coil Is the coil number for which the Power Management feedback is requested
    #@param device Defines the type of device for which we need the PM feedback
    def readPMFeedback(self,coil,device):
        print("In the read feedback")
        currentFeedback = int(surfaceObject.getPMStatus(coil,device))
        print("Current Feedback received in laptop Charging Policy: ",currentFeedback)
        if currentFeedback >330 :
            return 0
        
        elif currentFeedback < 320:
            return 1

    ##This method turns off the coil @param coil_number
    #@param self The object pointer
    #@param coil_number Is the coil number for which the Power Management feedback is requested
    #@param device Defines the type of device for which we need the PM feedback
    def terminateCoilCharging(self, coil_number,device):
        print("in the terminate charging")
        global surfaceObject
        surfaceObject.deactivateCoil(coil_number,device)

    ##This method charges a device until the device is removed
    #@param self The object pointer
    #@param x Feedback status from check Charging
    #@param coil Is the coil number for which the Power Management feedback is requested
    #@param device Defines the type of device for which we need the PM feedback

    ## TODO : Error LED implementation needed to be done after brainstorming session
    def continueCharging(self,x,coil,device):
        # global error_detectionObject
        
        # if (delay_L >= 4 ):
        #   error_detectionObject.delay_error(1)

        # else:
        #   error_detectionObject.delay_error(0)

        while x:
            x=self.checkCharging(coil,device)
        
        print("Delay_L: ", delay_L)
        self.terminateCoilCharging(coil,device)
        global_var.devices.remove(device)
        
