"""
Tests for calibrating a motor connected through an ESC, to check
if it works or to determine the PWM dutycycle/frequency.

V1.0.0
"""

from components.esc import ESC

PIN = 18
esc = ESC(PIN)

esc.initialise_motor()



while True:
    try:
        esc.set_dutycycle(int(input("Enter dutycycle integer : ")))
        #print(esc.get_throttle())
        # esc.set_frequency(int(input("Enter frequency: ")))

    except KeyboardInterrupt:
        esc.set_motor_speed(float(0))
        break
