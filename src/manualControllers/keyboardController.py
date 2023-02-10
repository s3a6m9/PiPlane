"""
Listens for keyboard presses and sends the plane server instructions.

By: s3a6m9
Version: 1.0
"""

from .utils import check_val
import keyboard

class PlaneKeyboardController:
    def __init__(self, component_server):
        keyboard.add_hotkey("up", self.pitch_up)
        keyboard.add_hotkey("down", self.pitch_down)
        keyboard.add_hotkey("left", self.tilt_left)
        keyboard.add_hotkey("right", self.tilt_right)

        keyboard.add_hotkey("shift", self.increase_throttle)
        keyboard.add_hotkey("ctrl", self.decrease_throttle)


        self.server = component_server

        self.throttle_change = 0.05  # 5%
        self.elevator_change = 0.025  # 2.5%
        self.aileron_change = 0.05

        self.throttle = 0  # 1 = max throttle, 0 = min throttle

        # might be different depending on servo direction
        self.elevator = 0.5  # 1 = max up, 0 = min up

        # These will need calibration
        self.left_aileron = 0.5  #  1 = max right, 0 = max left
        self.right_aileron = 0.5  #  1 = max right, 0 = max left
    
    def pitch_down(self):
        self.elevator = check_val(round(self.elevator - self.elevator_change, 4))
        print(self.server.send_instruction(f"E:{self.elevator},"))
    
    def pitch_up(self):
        self.elevator = check_val(round(self.elevator + self.elevator_change, 4))
        print(self.server.send_instruction(f"E:{self.elevator},"))
    

    # THESE NEED TO WORK INVERSELY TO TURN WELL
    def tilt_left(self):
        self.left_aileron = check_val(round(self.left_aileron - self.aileron_change, 4))   # May need to change - to +, for others too
        self.right_aileron = check_val(round(self.right_aileron + self.aileron_change, 4))
        print(self.server.send_instruction(f"L_A:{self.left_aileron},R_A:{self.right_aileron},"))

    def tilt_right(self):
        self.right_aileron = check_val(round(self.right_aileron - self.aileron_change, 4))
        self.left_aileron = check_val(round(self.left_aileron + self.aileron_change, 4))   # May need to change - to +, for others too
        print(self.server.send_instruction(f"L_A:{self.left_aileron},R_A:{self.right_aileron},"))
    
    def increase_throttle(self):
        self.throttle = check_val(round(self.throttle + self.throttle_change, 4))
        print(self.server.send_instruction(f"M:{self.throttle},"))

    def decrease_throttle(self):
        self.throttle = check_val(round(self.throttle - self.throttle_change, 4))
        print(self.server.send_instruction(f"M:{self.throttle},"))

        # Add pitch change with ailerons for more control
