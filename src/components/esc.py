"""
Controls electronic speed controllers that are connected to motor
By: s3a6m9
Version: 1.0
"""

import time
import pigpio


class ESC:
    """ Control the ESC to set motor speed """
    def __init__(
        self, pin, frequency=50, min_dutycycle=50900,
        max_dutycycle=94000, close_dutycycle=40000):

        self.pin = pin
        self.frequency = frequency

        self.min_duty = min_dutycycle
        self.max_duty = max_dutycycle

        self.margin = self.max_duty - self.min_duty

        self.close_dutycycle = close_dutycycle

        self.pi = pigpio.pi()
        self.pi.set_mode(self.pin, pigpio.OUTPUT)

        self.percentage_speed = None

    def initialise_motor(self):
        """
        *** WARNING, MAY START MOTOR at 10% SPEED ***
        Initialises the motor to start accepting signals
        """
        self.set_motor_speed(0.1)
        time.sleep(0.1)
        self.set_motor_speed(0)

    def set_motor_speed(self, percentage_speed):
        """
        Sets the speed for the motor

        percentage_speed should be in for e.g., 0.01 for 1% and 1 for 100%
        """
        dutycycle = int(
            round(self.min_duty + (self.margin * percentage_speed), 0))

        if percentage_speed == 0:
            dutycycle = self.close_dutycycle

        self.pi.hardware_PWM(self.pin, self.frequency, dutycycle)
        self.percentage_speed = percentage_speed

        # return dutycycle

    def get_throttle(self):
        """ Returns the throttle percentage speed """
        return self.percentage_speed
