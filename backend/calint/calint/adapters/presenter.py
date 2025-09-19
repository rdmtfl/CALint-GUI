from abc import abstractmethod

from calint.entities import Report
from calint.use_cases.ports import PrinterPort


class Presenter(PrinterPort):
    @abstractmethod
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def present(self, content: Report) -> None:
        raise "Method not implemented"

    @classmethod
    def show(cls, content: Report) -> None:
        cls.present(cls, content)
