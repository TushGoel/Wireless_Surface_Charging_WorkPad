from arduino_pin_mapping import*
from hardware_interface import *
from handler import *
import global_var
import time

hardwareInterfaceObject=hardware_interface()
handlerObject = handler()

##This class defines methods for switching ON/OFF coils and pin mapping with the micro-controller
class switching():

    ##Initializing function
    def __init__(self):
        print("In the init of _switching")
        self.type = None

    ##This method implements
    #@param self The object pointer
    #@param coil Is the coil number for which the Power Management feedback is requested
    #@param type Defines the type of device for which we need the PM feedback
    #@param status Defines whether the @param coil needs to be ON/OFF -> 1/0
    def coilPinMapping(self,coil,type,status):
        print("----------------------*************-------------------")
        print("In the coil pins mapping ")
        print("Data received: coil no.--> ", coil , " Device --> ",type)
        print("Status received --> ",status)
        self.type = type
        try:
            if(type == "Laptop"):
                global_var.pins = arduino_laptop[coil]
                print("Pins detected is--> ",global_var.pins)
                print("----------------------*************-------------------")

                if(status=='1\n'):
                    self.turnONCoil(status)

                elif (status=='0\n'):
                    self.turnOFFCoil(status)

            if(type == "Mobile 2"):
                global_var.pins = arduino_phone1[coil]
                print("Pins detected is--> ",global_var.pins)
                print("----------------------*************-------------------")
                if(status=='1\n'):
                    self.turnONCoil(status)

                elif (status=='0\n'):
                    self.turnOFFCoil(status)
                    
        except:
            print("Wrong data")

    ##This method turns ON coils based on @param status
    #@param self The object pointer
    #@param status Defines whether the @param coil needs to be ON/OFF -> 1/0
    def turnONCoil(self, status):
        print("In the turn on coil")
        print("Pins value in the turn on coil: ",global_var.pins)
        # global hardwareInterfaceObject
        # hardwareInterfaceObject.pinsManagement(global_var.pins,status)
        global handlerObject
        handlerObject.prioritizer(self.type, status)


    ##This method turns OFF coils based on @param status
    #@param self The object pointer
    #@param status Defines whether the @param coil needs to be ON/OFF -> 1/0
    def turnOFFCoil(self,status):
        print("In the turn off coil")
        print("Pins value in the turn off coil: ",global_var.pins)


        global handlerObject
        handlerObject.prioritizer(self.type, status)
        
    ##This method implements test code to be ignored
    #@param self The object pointer
    def checking_value_switching(self):
        print("Active sessions in switching: ")
        print("Coils: ",global_var.activeCoils)
        print("Devices: ", global_var.devices)
        print("Phone Session: ",global_var.sessionInProgress)
        global_var.activeCoils.remove(1)
        global_var.devices.remove("Laptop")
        del global_var.sessionInProgress[0]
        print("Active sessions in switching after change : ")
        print("Coils: ",global_var.activeCoils)
        print("Devices: ", global_var.devices)
        print("Phone Session: ",global_var.sessionInProgress)
        