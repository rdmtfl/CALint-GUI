from abc import ABC, abstractmethod
from typing import Dict


class CreateConfigPort(ABC):
    @abstractmethod
    def __init__(self) -> None:
        super().__init__()

    @classmethod
    @abstractmethod
    def get_config_input(cls, source) -> Dict:
        raise "method not implemented"
