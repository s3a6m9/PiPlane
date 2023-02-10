# PiPlane
Code for a self-flying plane powered by a Raspberry Pi

***
***Note, the code used for the sensors has not yet been tested for autonomous flight capabilities.
Furthermore, this project is still in development and should only be used as an example for understanding
some of the code required behind autonomous planes.***
***

<br>
<br>

**The hardware and electronics the code is developed for is as follows:**
- SG90 servos
- 40A Electronic Speed Controller (ESC) connected to a D2836/7 1120kv brushless motor
- UNO R3 arduino board for joystick and sliding potentiometer analogue readings (used as a manual controller)
- Raspberry Pi 3B +, used as the controller and autopilot computer
- WaveShare Sense B hat, used as an addon with the Raspberry Pi on the plane.
- E3372 4G USB dongle
It can be used with other servos or ESCs, but may require non default parameters and other configurations to operate safely and correctly.

<br>

**The functionalities of this code include:**
- Servo control
- Brushless motor ESC control
- Magnetometer heading calculation & calibration
- Accelerometer, gyroscope, magnetometer, barometer, thermometer readings
- Altitude calculation
- Long-range internet communication through socket servers
