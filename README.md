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
- Initializes all the parameters required for Laptop charging policy.
- Checks the feedback from the charging coils continuously and exits when not charging.
- Defines the type of device for which we need the feedback.
- Reads the feedback from the charging coils.
- Charges a device until the device is removed.

4.) Phone Charging Policy:
- Initializes all the parameters required for Phone charging policy.
- Checks the feedback from the charging coils continuously and exits when not charging.
- Defines the type of device for which we need the feedback.
- Reads the feedback from the charging coils.
- Charges a device until the device is removed.

5.) Surface:
- Determines the coil number to be activated from the x, y co-ordinates received from the sensing module.
- Gets neighboring coil numbers based on the region.
- Activates coil/s and updates active coils list.
- Uses power management for getting feedback for energy optimization.

6.) Switching:
- Switching ON/OFF coils and pin mapping with the micro-controller based on the status received.
- Controls electromagnetic charging coils.

7.) Handler:
- Implement queue to avoid overwriting and interference.
- Event handler for the arriving and departing events.

8.) Error Detection:
- Checks and verifies where the error and what kind of error occurs in the processing of the code.
- Logs the error.

9.) Hardware Interface:
- Establishing serial communication connection between Arduino and Raspberry Pi.
- Writes the data to the Arduino for turning the pin on and off according to the instructions received.
- Convertes the data into Arduino readable format before transmitting it to Arduino for completing the functionality.

10.) Arduino Pin Mapping:
- Contains the mapping of all the coils to the corresponding pins on the Arduino.


Also created high-level documentation for the code architecture on the Visual Paradigm software.