from abc import abstractmethod
from typing import Dict

from calint.use_cases.ports import CreateConfigPort


class SerializerAdapter(CreateConfigPort):
    @abstractmethod
    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    @abstractmethod
    def serialize(data: Dict) -> str:
        raise "method not implemented"

    @staticmethod
    @abstractmethod
    def deserialize(source: str) -> Dict:
        raise "method not implemented"

    @classmethod
    def get_config_input(cls, source):
        string = source.read()
        return cls.deserialize(string)
