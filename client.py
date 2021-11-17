import bisect
import socket
import time


class ClientError(Exception):
    """класс исключений клиента"""
    pass


class Client:
    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout

        try:
            self.connection = socket.create_connection((host, port), timeout)
        except socket.error as err:
            raise ClientError("Cannot create connection", err)

    def read(self):
        try:
            data = b""
            data += self.connection.recv(1024)
            #if data.decode() == "Заказ уже открыт":
            return data.decode()
        except socket.error as err:
            raise ClientError("Error reading data from socket", err)

    def send(self, data):
        try:
            self.connection.sendall(data)
        except socket.error as err:
            raise ClientError("Error sending data to server", err)

    def close(self):
        try:
            self.connection.close()
        except socket.error as err:
            raise ClientError("Error. Do not close the connection", err)
