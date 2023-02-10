"""
Collects the readings received through a Arduino UNO R3, and converts them 
into min/max percentage to send instructions to the plane server.

By: s3a6m9
Version: 1.0
"""
import serial
import time


class PlaneR3Controller:
    def __init__(
        self, device="/dev/ttyACM0", baud_rate=9600, 
        MAX_Y_JOYSTICK=1023, MAX_X_JOYSTICK=1023,
        BASE_Y_JOYSTICK=520, BASE_X_JOYSTICK=502,
        JOYSTICK_OFF_SWITCH_STATE=1, MAX_POTENTIOMETER=681 
        ):
            self.MAX_Y_JOYSTICK = MAX_Y_JOYSTICK
            self.MAX_X_JOYSTICK = MAX_X_JOYSTICK
            
            self.BASE_Y_JOYSTICK = BASE_Y_JOYSTICK
            self.BASE_X_JOYSTICK = BASE_X_JOYSTICK

            self.JOYSTICK_OFF_SWITCH_STATE = JOYSTICK_OFF_SWITCH_STATE

            self.MAX_POTENTIOMETER = MAX_POTENTIOMETER

            self.r3 = serial.Serial(device, baud_rate, timeout=1)
            time.sleep(2)

    def _get_joystick_percentage(self, x, y):
        """
        This is adjusted for servo controls.
        0.0 = 0% so therefore the minimum the servo can move
        1.0 = 100%, the maximum the servo can move
        """

        # Adjustments because the value of the joystick is 
        # not at the median of the min and max readings
        x_percentage = x / self.MAX_X_JOYSTICK + 0.008 
        y_percentage = y / self.MAX_Y_JOYSTICK - 0.007
        # We only need percentages from 0.1 - 0.9 because ailerons won't move more
        # than that



        return (round(x_percentage, 3), round(y_percentage, 3))

    def _get_potentiometer_percentage(self, potval):
        """
        0 = no thrust
        1 = max thrust
        """
        return round(potval / self.MAX_POTENTIOMETER, 3)

    def get_r3_values(self):
        values = self.r3.readline()
        if values:  # If there is a new reading
            decoded_values = values.decode("utf-8", "ignore")

            # Checks for data integrity.
            if decoded_values.count("s") != 1 or \
                decoded_values.count("e") != 1 or \
                 decoded_values.count(" ") != 3:
                    return None    

            decoded_values = \
                decoded_values.replace("s", "").replace("e", "").split()
            
            joystick_x, joystick_y, potentiometer, switch_state = \
                decoded_values

            return self._get_joystick_percentage(int(joystick_x), int(joystick_y)), \
                int(switch_state), self._get_potentiometer_percentage(int(potentiometer))

    def _raw_readings(self):
        values = self.r3.readline()
        if values:
            raw_values = values.decode("utf-8", "ignore")
            
            return raw_values

    def close_port(self):
        self.r3.close()

if __name__ == "__main__":
    # pip install pyserial
    # https://docs.arduino.cc/software/ide-v1/tutorials/Linux
    # sudo chmod a+rw /dev/ttyACM0
    r3 = PlaneR3Controller()

    while True:
        try:
            values = r3.get_r3_values()
            if not values:
                continue
            y, x = values[0]
            switch_state = values[1]
            potentiometer = values[2]

            print(f"\n X: {x}\n Y: {y}\nSwitch State: {switch_state},  Potentiometer: {potentiometer}")
        
        except KeyboardInterrupt:
            r3.close_port()
