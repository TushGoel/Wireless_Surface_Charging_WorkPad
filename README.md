# Wireless_Surface_Charging_WorkPad

Different Modules are designed for carrying out different functionality for end-to-end application. The modules are explained as follows:

1.) Sensing Module: 
- Processes the sensing readings and localizes devices for charging.
- Receives and processes the sensing readings from the Arduino.
- Predicts and localizes coils based on the prediction data.
- Checks the feedback from the charging coils continuously and exits when not charging.

2.) Orchestrator:
- Select charging policy according to type of device.
- Multi-threading has been implemented for simultaneous processes.

3.) Laptop Charging Policy:
- initializes all the parameters required for laptop charging policy
- checks the feedback from the charging coils continuously and exits when not charging 
- Defines the type of device for which we need the PM feedback
- reads the feedback from the charging coils and returns true when charging
- charges a device until the device is removed

4.) Phone Charging Policy:
- initializes all the parameters required for Phone charging policy
- checks the feedback from the charging coils continuously and exits when not charging 
- Defines the type of device for which we need the PM feedback
- reads the feedback from the charging coils and returns true when charging
- charges a device until the device is removed

5.) Surface:
- determines the coil number to be activated from the x, y co-ordinates received from the sensing module
- gets neighboring coil numbers based on @param region
- activates @param coil and updates active coils list
- sends command to get the Power Management feedback for the @param coil, receives and processes it
- use power management for getting feedback for energy optimization.

6.) Switching:
- switching ON/OFF coils and pin mapping with the micro-controller based on status
- Controls electromagnetic charging coils

7.) Handler:
- Implement queue -- no overwriting
- Event handler

8.) Error Detection:
- Checks and verifies where the error occurs in the processing
- Logs the error

9.) Hardware Interface:
- Establishing serial communication connection between arduino and raspberry pi
- Writes the data to the arduino for turning the pin on and off according to the instruction received
- Convertes the data into arduino readable format before transmitting it to arduino for completing the functionality

10.) Arduino Pin Mapping:
- contains the mapping of all the coils to the corresponding pins on the Arduino MEGA, G stands for GPIO


Also created high-level documentation for the code architecture on the Visual Paradigm software.