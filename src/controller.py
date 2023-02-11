"""
Sends instructions to the plane client.
These instruction are controller readings which
are used to control the plane manually


By: s3a6m9
Version: 1.0
"""
from connections import forPlaneServer
from manualControllers import R3Controller


HOST = "0.0.0.0"
PORT = 8034

controller = R3Controller.PlaneR3Controller()

def main():
    """ Main function """
    server = forPlaneServer.ComponentServer(HOST, PORT)
    print("Starting server\n")
    print(server.initialise_server())




    prev_LA = 0.5
    prev_RA = 0.5
    prev_E = 0.5
    prev_M = 0
    print("Running")
    while True:
        try:
            values = controller.get_r3_values()
            if not values:
                continue
            y, x = values[0]
            switch_state = values[1]
            potentiometer = values[2]

            x_max = 0.7 # max pushed up aileron
            x_min = 0.15 # Max Pulled down aileron

            y_max = 0.8 # pushed up, pitching down
            y_min = 0 # pulled down, so for pitch up

            y = round(1 - y, 4) # Inverting so pulling joystick back = pitch up
            
            if y > y_max:
                y = y_max
            elif y < y_min:
                y = y_min
            

            if x >= 0.5:
                left_aileron = round(1- x, 4) # aileron pulled down
                right_aileron = round(x, 4)  # pushed up
            if x < 0.5:
                left_aileron = round(1 - x, 4) # Create symmetrical turning between ailerons
                right_aileron = round(x, 4)

            if left_aileron > x_max:
                left_aileron = x_max
            elif left_aileron < x_min:
                left_aileron = x_min
            
            if right_aileron > x_max:
                right_aileron = x_max
            elif right_aileron < x_min:
                right_aileron = x_min

            if abs(prev_LA - left_aileron) < 0.005 and abs(prev_RA - right_aileron) < 0.005 \
                and abs(prev_E - y) < 0.005 and abs(prev_M - potentiometer) < 0.005:
                continue # Does not send instruction if it has not changed by more than 0.5%
            

            # check and compare to last values sent
            instruction = f"L_A:{left_aileron},R_A:{right_aileron},E:{y},M:{potentiometer}"
            server.send_instruction(instruction)
            print(instruction)
            prev_LA = left_aileron
            prev_RA = right_aileron
            prev_E = y
            prev_M = potentiometer            
        except KeyboardInterrupt:
            break

    server.close_connection()


if __name__ == "__main__":
    main()
