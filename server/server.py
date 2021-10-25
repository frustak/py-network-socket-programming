
from socket import AF_INET, SOCK_STREAM, socket


class Server:
    BUFFER_SIZE = 1024
    STATUS_SIZE = 128
    LENGTH_SIZE = 64
    OK_STATUS = b"200 ok".ljust(STATUS_SIZE)
    NOT_FOUND_STATUS = b"404 Not Found".ljust(STATUS_SIZE)

    address: str
    port: int
    _socket: socket

    def __init__(self, address: str, port: int) -> None:
        self.address = address
        self.port = port

    def setup(self) -> None:
        self._socket = socket(AF_INET, SOCK_STREAM)
        self._socket.bind((self.address, self.port))
        self._socket.listen()

    def start(self) -> None:
        while True:
            conn, addr = self._socket.accept()
            with conn:
                print(f"New Connection: {addr}")
                filename = conn.recv(self.BUFFER_SIZE).decode()
                try:
                    content = read_file_content(filename)
                    conn.sendall(self.OK_STATUS)
                    message_size = str(len(content)).ljust(self.LENGTH_SIZE)
                    conn.sendall(message_size.encode())
                    conn.sendall(content)
                except:
                    conn.sendall(self.NOT_FOUND_STATUS)

    def stop(self) -> None:
        self._socket.close()


def read_file_content(filename: str) -> bytes:
    with open(f"ServerFile/{filename}", "r") as file:
        return file.read().encode()


if __name__ == "__main__":
    server = Server(address="", port=12111)
    server.setup()
    print("Server is ready...")
    server.start()
    server.stop()
