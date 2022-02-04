from dataclasses import dataclass
from typing import NamedTuple, NewType
from threading import Thread


Package = NewType("Package", tuple[bytes, bytes])


class Message(NamedTuple):
    code: int
    time: int
    sender: str
    content: str


def start_thread(**kwargs):
    thread = Thread(**kwargs)
    thread.start()
