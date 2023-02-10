"""
Controls a connected servo
By: s3a6m9
Version: 1.0
"""

from gpiozero import Servo as gpiozero_servo
from gpiozero.pins.pigpio import PiGPIOFactory


class Servo:
    """ Class for controlling a servo """
    def __init__(self, pin, min_pulse=0.0005,
                 max_pulse=0.0025, frame_width=0.02):
        self.min_pulse = min_pulse
        self.max_pulse = max_pulse
        self.frame_width = frame_width
        self.pin = pin
        self.servo = None
        self.rotation_percentage = None

    def initialise_servo(self):
        """ Initialises servo for controlability """
        self.servo = gpiozero_servo(
            self.pin,
            pin_factory=PiGPIOFactory(),
            min_pulse_width=self.min_pulse,
            max_pulse_width=self.max_pulse,
            frame_width=self.frame_width,
        )
        self.set_rotation(0)

    def set_rotation(self, rotation_percentage):
        """ Rotates the servo obased on the percentage arg """
        rotation_value = 2 * rotation_percentage - 1
        # The value of 2 is used because servo value can only be between
        # -1 and 1 so 0% would be -1 and therefore the min angle
        self.servo.value = rotation_value
        self.rotation_percentage = rotation_percentage

    def turn_off(self):
        """ Turns off the servo """
        self.servo.value = None
        self.servo.close()
