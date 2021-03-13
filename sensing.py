from orchestrator import *

from global_var import *
from model_info import *

from keras.models import model_from_json
from sklearn.externals.joblib import load
import numpy as np

import time

## DONE: Time model loading.
#  1. Arch, weights                     ~ 5 seconds
#  2. Full model (Arch + Weights)       ~ 26 seconds
#  3. Model + transform together        ~ 6 seconds
#  3. Time b/w sensing init & b4 orchestrator:  
#     ~ 0.003 + 0.2 + 0.2 = ADC reading + Prediction + Correct (Non-zero) prediction


# Import scaler
tran_model = load(PATH['Transform'])
# Import model --> arch, weights

with open(PATH['Angle'][0],'r') as f: # Architecture
    model_angle = model_from_json(f.read())
model_angle.load_weights(PATH['Angle'][1]) # Weights

with open(PATH['Location'][0],'r') as f: # Architecture
    model_loctn = model_from_json(f.read())
model_loctn.load_weights(PATH['Location'][1]) # Weights 


handlerObject = handler()
orchestratorObject=orchestratorClass()


##This class defines all the functions for sensing through coils
class sensingClass():
    print("Inside the sensing class")

    ##Initializer
    def __init__(self):
        print("In the init of sensing class")
        self.data = None # Temp data from Arduino's serial port
        self.sample_ptr = 0
        self.sensors = np.zeros((5, 4)) # Will only have 5 timestamps of sensor values
        self.features = np.zeros((1, 8)) # Will have moving averages of features
        self.mobile1_sensors, self.mobile2_sensors, self.laptop_sensors = None, None, None
        self.tran_data = None # Transformed data -- Unused
        self.pred_data = None # Predicted data
        self.x, self.y = 0, 0
        global hardwareInterfaceObject
	    global handlerObject
        global error_detectionObject
        self.ser = hardwareInterfaceObject.initSerialComm_0() # Serial data recieved from Arduino
        
    ##This method processes the sensing readings and localizes devices for charging
    #@param self The object pointer
    def sensing_initializer(self):          
            while True:
                print("In the while loop of sensing initializer")
                st = time.time()
                self.getADCReadings()
        
                print("Time for reading: {:4f} seconds.".format(time.time()-st))
                print("Active devices: ",global_var.devices)
                self.deviceLocalization()
                print("Prediction Data: ", self.pred_data)
        
                if(self.pred_data):
                    print("Time for correct prediction: {:4f} seconds.".format(time.time()-st))
                    self.localizeDevice()
                else:
                    print("Nothing has been detected ")
                
                print("Came back in sensing intializer")
                
    ##This method receives and processes the sensing readings from the Arduino
    #@param self The object pointer
    def getADCReadings(self):
            self.data = handlerObject.receiver("S")
            
            print("Sensing data  from arduino: ", self.data)
            print(len(self.data))
                
            if(50 > len(self.data) > 35):

                error_detectionObject.ADC_error(0)

                self.data = self.data.decode()
                self.data = self.data.split(",")
                print("Values after decode: ", self.data)
                # String --> Floats
                for i, sval in enumerate(self.data[:4]):
                    self.sensors[self.sample_ptr, i] = float(sval)
                print("Values after floats:", self.sensors)
                if self.sample_ptr < 4:
                    self.sample_ptr += 1
                    self.getADCReadings()
                else:
                    self.features[0, :4] = np.mean(self.sensors[:4, :], axis=0)
                    self.features[0, -4:] = np.mean(self.sensors, axis=0)
                    self.sensors[:-1, :] = self.sensors[1:, :]

                ## Outlier check
                outlier = True
                print(outliers_limits['S1'][0], self.sensors[0], outliers_limits['S1'][1])
                if outliers_limits['S1'][0] >= self.sensors[0] >= outliers_limits['S1'][1]:
                    if outliers_limits['S2'][0] >= self.sensors[1] >= outliers_limits['S2'][1]:
                        if outliers_limits['S3'][0] >= self.sensors[2] >= outliers_limits['S3'][1]:
                            if outliers_limits['S4'][0] >= self.sensors[3] >= outliers_limits['S4'][1]:
                                print("Values are NOT outliers")
                                outlier = False
                                 
                            else:
                                print("S4 is outlier", self.sensors[3])
                        else:
                            print("S3 is outlier", self.sensors[2])
                    else:
                        print("S2 is outlier", self.sensors[1])
                else:
                    print("S1 is outlier", self.sensors[0])
                if outlier:
                    error_detectionObject.ADC_error(1)
                    self.getADCReadings()                



    ##This method predicts and localizes coils based on @param prediction_data
    #@param self The object pointer
    #@param prediction_data Data received from the machine learning model
    def localizeDevice(self):
        
        global orchestratorObject     
        global error_detectionObject
        print("In the localize device function")
        print(self.pred_data)


        if len(self.pred_data):
            error_detectionObject.sensing_error(0)
            if (self.pred_data[2] not in global_var.devices):
                global_var.devices.append(self.pred_data[2])
                print("Active devices: ",global_var.devices)
                global orchestratorObject
                orchestratorObject.initialization(self.pred_data)
       
            else:
                print(self.pred_data[2],"is already busy")

        else:
            error_detectionObject.sensing_error(1)
            print("No valid prediction data received")


        print("Current active devices:- ",global_var.devices)
        print("Current sessions in progress: ",global_var.sessionInProgress)

    ##This method checks the feedback from the charging coils continuously and exits when not charging
 
    ##This method checks the feedback from the charging coils continuously and exits when not charging
    #@param self The object pointer
    #@param data Sensing Data
    #@param values array holding sensing values
    def deviceLocalization(self):#, values):
            
        print("Mobile_1 features MA - ", self.features)
        st = time.time()
        self.tran_data = tran_model.transform(self.features) # Transformed data
        print("Transformed Mobile_1 features", self.tran_data)
        self.pred_data = model_loctn.predict(self.tran_data) # Predicted probabilities
        print("Location confidence", self.pred_data)
        self.pred_data = classes[np.argmax(self.pred_data)] # Max confidence class (Location)
        print("------ LOCTN:", self.pred_data)
        self.y = self.pred_data // 100
        self.x = self.pred_data % 100
        print("------ (X, Y): (%d, %d)" % (self.x, self.y))
        if self.x == 0 and self.y == 0:
            self.pred_data = None
        else:
            self.pred_data = (self.x, self.y, "Mobile 1")
        print("Time for predicting: {:4f} seconds.".format(time.time()-st))
        ### TODO: Set type of device based on grid location
        
    ##This method obtains max values for each sensing coils from first 1000 values
    # @param self The object pointer
    def checking_value_sensing(self):
        print("Active sessions in sensing: ")
        print("Coils: ",global_var.activeCoils)
        print("Devices: ", global_var.devices)
        print("Phone Session: ",global_var.sessionInProgress)
        global_var.activeCoils.append(1)
        global_var.devices.append('Phone')
        P1=PhonechargingPolicy()
        P1.check(1)
        global_var.sessionInProgress.append(P1)
        print("Active sessions in sensing after change: ")
        print("Coils: ",global_var.activeCoils)
        print("Devices: ", global_var.devices)
        print("Phone Session: ",global_var.sessionInProgress)    

   