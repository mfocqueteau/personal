from os import stat
import pickle
import socket as skt

from time import time
from utils import start_thread, Message, Package


def main():
    HOST = "localhost"
    PORT = 4000
    SERVER = ChatServer(HOST, PORT)
    SERVER.start()


class ChatServer:
    def __init__(self, host, port):
        self.host: str = host
        self.port: int = port
        self.socket = skt.socket(skt.AF_INET, skt.SOCK_STREAM)
        self.socket.setsockopt(skt.SOL_SOCKET, skt.SO_REUSEADDR, 1)

        self.clients: dict[str:object] = {}

    def add_new_client(self, new_client):
        data = self.build_message("clients_list", list(self.clients.keys()))
        self.send(new_client, data)
        message = self.recv(new_client)
        self.clients[message.content] = new_client
        print(f"{message.sender} has joined the chat")

    def bind(self):
        for _ in range(100):
            try:
                self.socket.bind((self.host, self.port))
            except OSError:
                self.port += 1

    @staticmethod
    def build_message(code, content) -> Package:
        message = Message(code, time(), "server", content)
        serialized = pickle.dumps(message)
        length = len(serialized).to_bytes(4, "big")
        return length, serialized

    def handle_user_left(self, socket):
        for key, value in self.clients.items():
            if value == socket:
                del self.clients[key]
                print(f"{key} has left the chat")

    def listener_thread(self, client_socket):
        while True:
            try:
                length = client_socket.recv(4)
                data = client_socket.recv(int.from_bytes(length, "big"))
                message = pickle.loads(data)
            except EOFError or BrokenPipeError:
                break

            if message.code == "global":
                self.send_clients((length, data))
        self.handle_user_left(client_socket)

    def recv(self, socket) -> Message:
        length = socket.recv(4)
        data = socket.recv(int.from_bytes(length, "big"))
        if not data:
            ("Lost connection")
        message = pickle.loads(data)
        return message

    @staticmethod
    def send(socket, data: Package):
        for item in data:
            socket.sendall(item)

    def send_clients(self, data):
        for client_socket in self.clients.values():
            self.send(client_socket, data)

    def start(self):
        self.bind()
        self.socket.listen(5)
        print("Listening...")
        try:
            while True:
                client, _ = self.socket.accept()
                self.add_new_client(client)
                start_thread(target=self.listener_thread, args=(client,), daemon=True)
        except KeyboardInterrupt:
            print()
            exit()


if __name__ == "__main__":
    main()
