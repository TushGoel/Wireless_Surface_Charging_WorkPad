import logging
import global_var
from Phone_ChargingPolicy import *
from Laptop_ChargingPolicy import *
import threading
import time

class orchestratorClass():
    
    def __init__(self):
        print("In the init of orchestrator")

    # Implemented by Tushar
    ## Multi-threading logic need to be tested    
    def initialization(self,locationData): # Initialization function to select charging policy according to type of device.
        
        if(len(global_var.sessionInProgress)<5) and (locationData[2]=="Mobile 1"):
            print("Location data in orchestrator ",locationData)
            if(locationData[2] in global_var.devices):
                P1=PhonechargingPolicy(locationData)
                global_var.sessionInProgress.append(P1)
                global t_start_M1
                t_start_M1 = time.time()
                P1.start()
                
                print("I came back in orchestrator")
            
            if locationData[2] not in global_var.devices:
                if P1 in global_var.sessionInProgress:
                    del global_var.sessionInProgress[global_var.sessionInProgress.index(P1)]
                    
            print("Current sessions in progress: ",global_var.sessionInProgress)

        elif(len(global_var.sessionInProgress)<5) and (locationData[2]=="Mobile 2"):
            print("Location data in orchestrator ",locationData)
            if(locationData[2] in global_var.devices):
                P2=PhonechargingPolicy(locationData)
                global_var.sessionInProgress.append(P2)
                global t_start_M2
                t_start_M2 = time.time()
                P2.start()
                print("Session activated: ",global_var.sessionInProgress)
                
                print("I came back in orchestrator")
            
            if locationData[2] not in global_var.devices:
                if P2 in global_var.sessionInProgress:
                    del global_var.sessionInProgress[global_var.sessionInProgress.index(P2)]
                    
            print("Current sessions in progress: ",global_var.sessionInProgress)

        elif(len(global_var.sessionInProgress)<5) and (locationData[2]=="Mobile 3"):
            print("Location data in orchestrator ",locationData)
            if(locationData[2] in global_var.devices):
                P3=PhonechargingPolicy(locationData)
                global_var.sessionInProgress.append(P3)
                global t_start_M2
                t_start_M2 = time.time()
                P3.start()
                print("Session activated: ",global_var.sessionInProgress)
                
                print("I came back in orchestrator")
            
            if locationData[2] not in global_var.devices:
                if P3 in global_var.sessionInProgress:
                    del global_var.sessionInProgress[global_var.sessionInProgress.index(P3)]
                    
            print("Current sessions in progress: ",global_var.sessionInProgress)

        elif(len(global_var.sessionInProgress)<5) and (locationData[2]=="Mobile 4"):
            print("Location data in orchestrator ",locationData)
            if(locationData[2] in global_var.devices):
                P4=PhonechargingPolicy(locationData)
                global_var.sessionInProgress.append(P4)
                global t_start_M2
                t_start_M2 = time.time()
                P4.start()
                print("Session activated: ",global_var.sessionInProgress)
                
                print("I came back in orchestrator")
            
            if locationData[2] not in global_var.devices:
                if P4 in global_var.sessionInProgress:
                    del global_var.sessionInProgress[global_var.sessionInProgress.index(P4)]
                    
            print("Current sessions in progress: ",global_var.sessionInProgress)


        elif(len(global_var.sessionInProgress)<5) and (locationData[2]=="Laptop"):
            print("Location data in orchestrator ",locationData)
            if(locationData[2] in global_var.devices):
                L1=LaptopchargingPolicy(locationData)
                global_var.sessionInProgress.append(L1)
                global t_start_L
                t_start_L = time.time()
                L1.start()
                print("Session activated: ",global_var.sessionInProgress)
                print("I came back in orchestrator")
                
            
            if locationData[2] not in global_var.devices:
                if L1 in global_var.sessionInProgress:
                    del global_var.sessionInProgress[global_var.sessionInProgress.index(L1)]            
            
            print("Current sessions in progress: ",global_var.sessionInProgress)
        
        elif(len(global_var.sessionInProgress)>=2):
            ("No more devices can be charged")
            
        else:
            print("No device has been detected")
            
        print("Current sessions in progress: ",global_var.sessionInProgress)