from _switching import*
import global_var
from error_detection import *
from arduino_pin_mapping import *

switchingObject = switching()
handlerObject = handler()
error_detectionObject = error_detection()

class surface():

    ##initialization
    def __init__(self):
        global handlerObject
        self.receiver = None
        self.PM = 0
        self.data = None

    ##This method determines the coil number to be activated from the x, y co-ordinates received from the sensing module
    #@param self The object pointer
    #@param location_data Contains x,y co-ordinates and device type
    def locationCoilsMapping(self,location_data):
        coil=0
        print("In the location coils mapping of the surface")
        print("Data received: x = ", location_data)

        try:
                
            if(location_data[2] == "Mobile 1"):
                coil = mobile1_location_coil[location_data[:2]]
     
            if(location_data[2] == "Laptop"):
                coil = laptop_location_coil[location_data[:2]]
                
            if(location_data[2] == "Mobile 2"):
                coil = mobile2_location_coil[location_data[:2]]
                
        except KeyError:
            print("No proper grid location detected or %s is mis-aligned", location)

        print("coils detected by the location coils mapping --> ",coil)
        print("--------------------------------------------------------------------")
        
        region=self.getChargingRegion(coil, location_data[2])

        return [coil,region]

    ##This method gets neighboring coil numbers based on @param region
    #@param self The object pointer
    #@param region Defines the set of coils together
    def getNeighbourCoils(self,region):
        neighbouringCoils = region_neighbor_coils[region]
        print("Neighboring coils rerturned are: ",neighbouringCoils)
        return neighbouringCoils

    ##This method activates @param coil and updates active coils list
    #@param self The object pointer
    #@param coil Is the coil number
    #@param device Defines Device type
    def activateCoil(self,coil,device):
        print("----------------------*************----------------------")
        print("In the activate coil the coil no. received --> ",coil)
        if coil not in global_var.activeCoils:
            global_var.activeCoils.append(coil)
            print("Current active coils: ",global_var.activeCoils)
        global switchingObject
        switchingObject.coilPinMapping(coil,device,'1\n')
        
    ##This method gets currently active coils
    #@param self The object pointer
    def getActiveChargingCoils(self):
        return global_var.activeCoils

    ##This method sends command to get the Power Management feedback for the @param coil, receives and processes it
    #@param self The object pointer
    #@param coil Is the coil number
    #@param device Defines Device type
    def getPMStatus(self,coil,device):
        print("In the getPM status function") 
        if (device=="Mobile 1"):
            self.data="P,1\n"
        
        elif (device=="Mobile 2"):
            print("Inside PM 2")
            self.data="P,2\n"
        
        elif (device=="Laptop"):
            self.data="P,3\n"
        
        handlerObject.prioritizer(device, self.data)
        
        while self.PM == 0:
            self.receiver = handlerObject.receiver("PMF")          
            print("Above decode condition")
            print("Feedback data received from arduino: ", self.receiver)
            print("feedback after parsing into integer: ", self.receiver)
            if(50 > len(self.receiver) > 30):
                error_detectionObject.hardware_interface_error(0)
                try:
                    error_detectionObject.hardware_interface_error(0)
                    print("Status Data received from arduino: ", self.receiver)
                    self.receiver = self.receiver.decode()
                    self.sensors = statusPM.split(",")
                    self.PM = int(self.sensors[-1])
                    print("After decoding feedback data: ", self.PM)
                  
                    print("Reading after decoding: ", self.PM)
                    if (self.PM != 0):
                        print("Reading of feedback to be sent: ", self.PM)
                        return self.PM
            
                except:
                    error_detectionObject.hardware_interface_error(1)
                    pass

            else:
                error_detectionObject.hardware_interface_error(1)
                pass

    ##This method turns OFF the @param coil
    #@param self The object pointer
    #@param coil Is the coil number
    #@param device Defines Device type
    def deactivateCoil(self,coil,device):
        global_var.activeCoils.remove(coil)
        global switchingObject
        switchingObject.coilPinMapping(coil,device,'0\n')

    ##This method maps set of coils to particular regions
    #@param self The object pointer
    #@param coil Is the coil number
    #@param device Defines Device type
    def getChargingRegion(self,coil,device):
        region=0
        if (device == "Mobile 2"):
            for key in coil_region.keys():
                if coil in key:
                    region = coil_region[key]
        return region
        