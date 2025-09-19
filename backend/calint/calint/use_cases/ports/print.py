from abc import ABC, abstractmethod


class PrinterPort(ABC):
    @abstractmethod
    def __init__(self) -> None:
        super().__init__()

    @classmethod
    @abstractmethod
    def show(cls, content):
        raise "method not implemented"
