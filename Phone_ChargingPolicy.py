import logging
import threading
import datetime
import time
from _surface import *
import global_var
from error_detection import *

error_detectionObject=error_detection()

surfaceObject=surface() #global surface class object creation

class PhonechargingPolicy(threading.Thread):
    i=0
    localization_data=[]

    def __init__(self,locationData):
        threading.Thread.__init__(self)
        self.localization_data=locationData

    def check(self,i):
        print("Here: ",i)
    
    def run(self): #Phone charging policy process start
        global error_detectionObject
        print("sessions in progress: ",global_var.sessionInProgress) #sessions in progress
        print("data received in initCharging of PhonechargingPolicy: ",self.localization_data) #localization data received in the format of : x,y,device
        print("In the init_charging policy")
        global surfaceObject
        device=self.localization_data[2] #making the device copy of the device received from sensing module
        coil,region=surfaceObject.locationCoilsMapping(self.localization_data) #identifying coil and region by interpreting the location parameters i.e. x,y
        neighbouringCoils=[] #local variable to store neighboring coils
    
        if not neighbouringCoils:
            print("Region received from surface: ",region)
            
            neighbouringCoils = surfaceObject.getNeighbourCoils(region) #getting neighboring coils according to the region
            print("Neighbouring coils received from surface are: ",neighbouringCoils)
            
            surfaceObject.activateCoil(coil,device) #activating the coil that is mapped to the location data given by sensing model
            
            print("I am back in Phone Charging Policy after activating the coils ")
            print("Current active coils: ",global_var.activeCoils) #list of active coils
            print("Current active devices: ",global_var.devices) #list of active devices
        
        x1 = self.checkCharging(coil,device) #checking if the coil detected by sensing is really charging the device or not
        
        if x1==0:
            self.terminateCoilCharging(coil,device) #switch off the coil as it is not charging the device
            neighbouringCoils.remove(coil)
            
            if neighbouringCoils:
                print("New Coil sent--> ",neighbouringCoils[0]) #the coil which is to be turned on
                surfaceObject.activateCoil(neighbouringCoils[0],device) # activate the neighbor 
                x2=self.checkCharging(neighbouringCoils[0],device) #Checking if the neighbor coil is really charging the device or not
                
                if x2==0:
                    self.terminateCoilCharging(neighbouringCoils[0],device) #switch off the coil as it is not charging the device
                    print("New Coil sent--> ",neighbouringCoils[1]) #the coil which is to be turned on
                    surfaceObject.activateCoil(neighbouringCoils[1],device) # activate the neighbor 
                    x3=self.checkCharging(neighbouringCoils[1],device) #Checking if the neighbor coil is really charging the device or not
                    
                    if x3==0:
                        self.terminateCoilCharging(neighbouringCoils[1],device) # Switch off the coil as it is not charging the device
                        global_var.devices.remove(device) #remove the device from active devices
                        error_detectionObject.neighboring_error(1)           
                        print("Device is mis-aligned") #device is mis-aligned
                        
                    else:
                        self.continueCharging(x3,neighbouringCoils[1],device) #charging is continued
                        error_detectionObject.neighboring_error(0)
                else:
                    self.continueCharging(x2,neighbouringCoils[0],device) #charging is continued
                    error_detectionObject.neighboring_error(0)    
        
        ## Implemented by Tushar
        else:
            self.continueCharging(x1,coil,device) #charging is continue
            error_detectionObject.neighboring_error(0)
                
    def checkCharging(self,coil,device): #Function to check if the activate coil is charging or not.
        print("In the check charging")
        x=1
        while x:
            x=self.readPMFeedback(coil,device) # Reading PM Feedback of the activated coil
            return x
        return 0

    def readPMFeedback(self,coil,device): #Function to take PM feedback readings and checking whether it is charging or not.
        print("In the read PM feedback")
        ## REDUNDANT INT CASTING -- REMOVE LATER
        currentFeedback = int(surfaceObject.getPMStatus(coil,device)) #get the current sensor readings
        print("Current Feedback is: ",currentFeedback)
        
        ## Implemented by Tushar

        global error_detectionObject
        
        if(700 < currentFeedback || currentFeedback < 300 || len(currentFeedback) == 0):
            error_detectionObject.power_management_feedback_error(0)
        
            ## THRESHOLDS
            if currentFeedback > 610: #checking if it lies in the charging region or not
                return 0
            elif currentFeedback < 600:
                return 1

        else:
            error_detectionObject.power_management_feedback_error(1)


    def terminateCoilCharging(self, coil_number,device): #turn off the coil which is not charging the device
        print("In the terminate charging coil")
        global surfaceObject
        surfaceObject.deactivateCoil(coil_number,device)

    def continueCharging(self,x,coil,device): #Charging is continued until device is removed
        global error_detectionObject
#         global t_start_M1
#         global t_start_M2
        
#         if (device == "Mobile 1"):
# #             global t_end_M1 
# #             t_end_M1 = time.time()
# #             global delay_M1
# #             delay_M1 = t_end_M1 - t_start_M1
# 
#         if (device == "Mobile 2"):
#             global t_end_M2 
#             t_end_M2 = time.time()
#             global delay_M2
#             delay_M2 = t_end_M2 - t_start_M2

        # if (delay_M >= 4 or delay_M2 >= 4):
        #   error_detectionObject.delay_error(1)

        # else:
        #   error_detectionObject.delay_error(0)


        ## TODO: Set global flag to tell prioritizer to dequeue.
        ## TODO: Implement error logic on this function
        while x:
            x=self.checkCharging(coil,device)
        
#         print("Delay_M1: ", delay_M1)
#         print("Delay_M2: ", delay_M2)
        self.terminateCoilCharging(coil,device)# Switch off the coil as it is not charging the device anymore
        global_var.devices.remove(device) #remove the device from active devices