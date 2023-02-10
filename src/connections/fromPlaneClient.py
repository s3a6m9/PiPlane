import socket


class ComponentClient():
    """ Class for controlling the components on the plane over the internet """
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def initialise_connection(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.host, self.port))

    def listen_data(self):
        while True:
            self.data = self.client.recv(1024)
            if self.data:
                yield self.data.decode("utf-8")

    def send_data(self, data):
        self.client.sendall(data)
