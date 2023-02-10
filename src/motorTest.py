"""
Code for testing a motor connected through an ESC, to check
if it works or to determine the PWM dutycycle/frequency.
"""
from components.esc import ESC

PIN = 18
esc = ESC(PIN, frequency=50, min_dutycycle=50900, max_dutycycle=94000, close_dutycycle=40000)

esc.initialise_motor()


# Note this may be dangerous as the brushless motor may have a different dutycycle or frequency.
# This means it can behave in unexpected ways.
while True:
    try:
        esc.set_motor_speed(float(input("Enter decimal percentage speed: ")))
        print(esc.get_throttle())
    except KeyboardInterrupt:
        esc.set_motor_speed(0.0)
        break
