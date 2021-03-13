##Global array containing all the active devices currently charging
global devices
devices=[]

##Global array containing all the coils activated for charging or localizing a device
global activeCoils
activeCoils=[]

##Global array containing the number of sensing coils currently active
global activeSensingCoils
activeSensingCoils=[]

##Global array containing the the number of charging sessions currently in progress
global sessionInProgress
sessionInProgress=[]

##Global array containing the the number of charging sessions currently in progress
global sessionInProgress_2
sessionInProgress_2=[]

##Global variable containing the pin number to be activated
global pins
pins=None

global t_start_M1 
t_start_M1=0

global t_start_M2
t_start_M2=0

global t_start_L
t_start_L=0

global t_end_M1 
t_end_M1=0

global t_end_M2 
t_end_M2=0

global t_end_L 
t_end_L=0

global delay_M1
delay_M1=0

global delay_M2
delay_M2=0

global delay_L
delay_L=0

## TODO: Add variable charging on status for handler's prioritizer
global charging_status
charging_status = 0
