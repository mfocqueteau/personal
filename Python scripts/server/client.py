import sys
import pickle
import socket as skt

from time import time
from dataclasses import dataclass
from utils import start_thread, Message


def main():
    CLIENT = Client("localhost", 7000, 4000)
    CLIENT.start()


@dataclass
class Client:
    host: str
    port: int
    server_port: int

    username: str = ""
    socket: skt.socket = skt.socket(skt.AF_INET, skt.SOCK_STREAM)

    def start(self):
        self.bind()
        self.socket.connect((self.host, self.server_port))
        self.set_username()

        start_thread(target=self.listener_thread, daemon=True)
        start_thread(target=self.sender_thread)

    def set_username(self):
        for i, arg in enumerate(sys.argv):
            if arg == "-u":
                self.username = sys.argv[i + 1]
        client_list = self.recv().content
        while True:
            self.username = (
                self.username if self.username else input("Ingrese nombre de usuario: ")
            )
            if len(self.username) < 3:
                print("Error: el nombre de usuario debe tener al menos tres caracteres")
            elif self.username in client_list:
                print("Error: el nombre ya está ocupado")
            else:
                break
            self.username = ""
        bytes_username = self.build_message("username", self.username)
        self.send(bytes_username)

    def bind(self):
        for _ in range(100):
            try:
                self.socket.bind(("0.0.0.0", self.port))
                break
            except OSError:
                self.port += 1
        else:
            self.socket.bind(("0.0.0.0", self.port + 1))

    def recv(self) -> Message:
        length = self.socket.recv(4)
        data = self.socket.recv(int.from_bytes(length, "big"))
        if not data:
            exit()
        message = pickle.loads(data)
        return message

    def send(self, data: tuple[bytes, bytes]):
        for item in data:
            self.socket.sendall(item)

    def sender_thread(self):
        while True:
            client_input = input()
            message = self.build_message("global", client_input)
            self.send(message)

    def build_message(self, code, content) -> tuple[bytes, bytes]:
        message = Message(code, time(), self.username, content)
        serialized = pickle.dumps(message)
        length = len(serialized).to_bytes(4, "big")
        return length, serialized

    def listener_thread(self):
        while True:
            try:
                code, _, sender, content = self.recv()
                if code == "global":
                    print(f"{sender}: {content}")
            except EOFError:
                exit()


if __name__ == "__main__":
    main()
