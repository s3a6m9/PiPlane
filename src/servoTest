"""
Testing script used for calibrating and studying connected servos.
"""

from components.servo import Servo
from time import sleep

servo1 = Servo(18, min_pulse=0.0005, max_pulse=0.0025, frame_width=0.02)
#servo2  = Servo(19)

servo1.initialise_servo()
#servo2.initialise_servo()

while True:
    try:
        servo1.set_rotation(float(input("(servo1) Enter Rotation percentage (decimal format, 0=min, 1=max): ")))
#        servo2.set_rotation(float(input("(servo2) Enter Rotation percentage (decimal format, 0=min, 1=max): ")))
#        servo2.set_rotation(0)
#        sleep(0.5)
#        servo2.set_rotation(1)


    except KeyboardInterrupt:
        break

servo1.turn_off()
#servo2.turn_off()
