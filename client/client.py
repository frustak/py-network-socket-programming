
from __future__ import annotations
from socket import AF_INET, SOCK_STREAM, socket


class Client:
    BUFFER_SIZE = 1024
    STATUS_SIZE = 128
    LENGTH_SIZE = 64

    address: str
    port: int
    _socket: socket

    def __init__(self, address: str, port: int) -> None:
        self.address = address
        self.port = port

    def connect(self) -> None:
        self._socket = socket(AF_INET, SOCK_STREAM)
        self._socket.connect((self.address, self.port))

    def send(self, message: str) -> None:
        encoded = message.encode()
        self._socket.sendall(encoded)

    def receive(self) -> str:
        message = self._socket.recv(self.BUFFER_SIZE)
        return message.decode("latin1")

    def receive_status(self) -> str:
        message = self._socket.recv(self.STATUS_SIZE)
        return message.decode().strip()

    def receive_length(self) -> int:
        message = self._socket.recv(self.LENGTH_SIZE)
        return int(message.decode().strip())

    def close(self) -> None:
        self._socket.close()


if __name__ == "__main__":
    filename = input("File Name: ")
    pathname = input("Path Name: ")

    client = Client(address='127.0.0.1', port=12111)
    client.connect()

    client.send(filename)
    status = client.receive_status()
    print(f"Status: {status}")

    if status == "200 ok":
        message_length = client.receive_length()
        message = ""
        while len(message) < message_length:
            message += client.receive()
        with open(pathname, "w") as file:
            file.write(message)

    client.close()
