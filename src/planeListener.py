"""
Waits for instructions from the server and controls the components

By: s3a6m9
Version: 1.0
"""
from connections import fromPlaneClient
from components import esc, servo
from time import sleep

HOST = "IP ADDRESS"
PORT = 8034

MOTOR_PIN = 18
LEFT_AILERON_PIN = 19
RIGHT_AILERON_PIN = 12
ELEVATOR_PIN = 13


sleep(5) # so that if program crashes it does not keep fucking up
print("Connecting")
client = fromPlaneClient.ComponentClient(HOST, PORT)
client.initialise_connection()
print("Connected")

motor = esc.ESC(MOTOR_PIN)

motor.initialise_motor()

left_aileron = servo.Servo(LEFT_AILERON_PIN)
right_aileron = servo.Servo(RIGHT_AILERON_PIN)
elevator = servo.Servo(ELEVATOR_PIN)

left_aileron.initialise_servo()
right_aileron.initialise_servo()
elevator.initialise_servo()

def stop_components():
    left_aileron.turn_off()
    right_aileron.turn_off()
    elevator.turn_off()

    motor.set_motor_speed(0)

running = True
while running:
    try:
        for instructions in client.listen_data():
            original_instructions = instructions

            instructions = instructions.split(",")
            print(instructions)

            for instruction in instructions:
                print(instruction)
                if ":" in instruction:
                    instruction = instruction.split(":")
                    component = instruction[0]

                    try:
                        component_value = float(instruction[1])
                    except ValueError:
                        continue

                    component_value = float(instruction[1])

                    # if instruction incomplete don't crash

                    # if elif used instead of match/case because raspberry pi
                    # still uses python version <3.10, will be updated.
                    if component == "M":
                        motor.set_motor_speed(component_value)

                    elif component == "L_A":
                        left_aileron.set_rotation(component_value)

                    elif component == "R_A":
                        right_aileron.set_rotation(component_value)

                    elif component == "E":
                        elevator.set_rotation(component_value)

            if instruction == "shutdown":
                running = False
                break


    except Exception as e:
        print(e)
        print("\n\tRestarting connection")
        client.initialise_connection()

stop_components()
print("Quitted")
