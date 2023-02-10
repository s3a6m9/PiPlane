"""
Acts as a server for the plane client to connect to. 
Allows for long range communication.

By: s3a6m9
Version: 1.0
"""

import socket

class ComponentServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def initialise_server(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET ,socket.SO_REUSEPORT, 1)

        self.server.bind((self.host, self.port))
        self.server.listen()
        self.conn, self.addr = self.server.accept()
        #print(f"Connected by {self.addr}")
        return self.conn, self.addr

    def send_instruction(self, instruction):
        try:
            self.conn.sendall(instruction.encode())
            return instruction
        #except socket.error
        except Exception as e:
            print(e)
            self.conn.close()
            self.initialise_server()
            return None

    def close_connection(self):
        self.conn.close()
