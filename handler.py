from hardware_interface import *
import time

hardwareInterfaceObject = hardware_interface()

class handler():

    ## Implemented by Aditya
    def __init__(self):
        print("In handler class")
        global hardwareInterfaceObject
        self.ser = hardwareInterfaceObject.initSerialComm_0() # Serial data recieved from Arduino
        self.data = {'Sensors': None, 'PMF': None}
        self.queue = [None, None, None, None, None]
        self.queue_head = 0
        self.queue_tail = 0
        self.status = ("1\n", "0\n", "P,1\n", "P,2\n", "P,3\n") ## Correct status possibilities
        self.tx_data = None ## Data to be transmitted to Arduino
        
    # Implemented by Aditya and Tushar
    ## Logic need to be tested and implemented w.r.t to errordetection module
    def prioritizer(self, device, status):
        ## Implement queue -- no overwriting
        if status in self.status:
            ## ENQUEUE
            self.queue[self.queue_tail] = (device, status)
            self.queue_tail += 1
            if self.queue_tail == len(self.queue) - 1:
                self.queue_tail = 0
            
            ## DEQUEUE -- Check global vars
            self.transmitter(self.queue[self.queue_head][1]) ## Transmit status
            self.queue_head += 1
            if self.queue_head == len(self.queue) - 1:
                self.queue_head = 0

    # Implemented by Aditya
    def transmitter(self, status):
        if status in self.status:
            if status in self.status[:2]:
                hardwareInterfaceObject.pinsManagement(global_var.pins, status)
            else:
                ## PM STATUS
                print("Data to be sent to arduino: ", status)
                self.tx_data = status.encode()
                print("The data sent to arduino: ", self.tx_data)
                ser.reset_input_buffer()
                ser.write(send_data)
                time.sleep(0.05)
        else:
            print ("Incorrect data to be sent !")

    # Implemented by Tushar
    def receiver(self, source):
        if source == "S":
            self.data['Sensors'] = self.ser.readline() 
            return self.data['Sensors']
        if source == "PMF": # TODO: and frequency
                            # First time instantly --> needs flag
            self.data['PMF'] = self.ser.readline()
            return self.data['PMF']
