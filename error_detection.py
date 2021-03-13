from hardware_interface import*

hardwareInterfaceObject=hardware_interface()


class error_detection():
    global hardwareInterfaceObject

    ## TODO : Need to updated according to the scheduler operation
    ser=hardwareInterfaceObject.initSerialComm_1()
        
    def __init__(self):
        pass

    def sensing_error(self,status): 
        error="ES,"+status+"\n"
        print("Error signal to be sent to arduino: ",error)
        send_error=error.encode()
        print("The error signal after encoding to send to arduino: ",send_error)
        ser.reset_input_buffer()
        ser.write(send_error)

    def power_management_feedback_error(self,status): 
        error="EP,"+status+"\n"
        print("Error signal to be sent to arduino: ",error)
        send_error=error.encode()
        print("The error signal after encoding to send to arduino: ",send_error)
        ser.reset_input_buffer()
        ser.write(send_error)


    def charging_error(self,status): 
        error="EC,"+status+"\n"
        print("Error signal to be sent to arduino: ",error)
        send_error=error.encode()
        print("The error signal after encoding to send to arduino: ",send_error)
        ser.reset_input_buffer()
        ser.write(send_error)

    def hardware_interface_error(self,status): 
        error="EH,"+status+"\n"
        print("Error signal to be sent to arduino: ",error)
        send_error=error.encode()
        print("The error signal after encoding to send to arduino: ",send_error)
        ser.reset_input_buffer()
        ser.write(send_error)

    def temperature_error(self,status): 
        error="ET,"+status+"\n"
        print("Error signal to be sent to arduino: ",error)
        send_error=error.encode()
        print("The error signal after encoding to send to arduino: ",send_error)
        ser.reset_input_buffer()
        ser.write(send_error)

    def neighboring_error(self,status): 
        error="EM,"+status+"\n"
        print("Error signal to be sent to arduino: ",error)
        send_error=error.encode()
        print("The error signal after encoding to send to arduino: ",send_error)
        ser.reset_input_buffer()
        ser.write(send_error)

    def type_of_device_error(self,status): 
        error="ED,"+status+"\n"
        print("Error signal to be sent to arduino: ",error)
        send_error=error.encode()
        print("The error signal after encoding to send to arduino: ",send_error)
        ser.reset_input_buffer()
        ser.write(send_error)

    def delay_error(self,status): 
        error="EW,"+status+"\n"
        print("Error signal to be sent to arduino: ",error)
        send_error=error.encode()
        print("The error signal after encoding to send to arduino: ",send_error)
        ser.reset_input_buffer()
        ser.write(send_error)

    def power_supply_error(self,status): 
        error="EV,"+status+"\n"
        print("Error signal to be sent to arduino: ",error)
        send_error=error.encode()
        print("The error signal after encoding to send to arduino: ",send_error)
        ser.reset_input_buffer()
        ser.write(send_error)

    def external_object_error(self,status): 
        error="EO,"+status+"\n"
        print("Error signal to be sent to arduino: ",error)
        send_error=error.encode()
        print("The error signal after encoding to send to arduino: ",send_error)
        ser.reset_input_buffer()
        ser.write(send_error)

    def ADC_RX_error(self,status): 
        error="EA,"+status+"\n"
        print("Error signal to be sent to arduino: ",error)
        send_error=error.encode()
        print("The error signal after encoding to send to arduino: ",send_error)
        ser.reset_input_buffer()
        ser.write(send_error)
