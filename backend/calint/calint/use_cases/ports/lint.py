from abc import ABC, abstractmethod

from calint.entities import LocalConfig, Report


class LintPort(ABC):
    @abstractmethod
    def __init__(self) -> None:
        super().__init__()

    @classmethod
    @abstractmethod
    def get_lint_output(cls, config: LocalConfig) -> Report:
        raise "method not implemented"
