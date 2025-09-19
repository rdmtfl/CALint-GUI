from dataclasses import dataclass
from typing import List

from .module import Module
from .broken_rule import BrokenRule


class Report:
    def __init__(self) -> None:
        self.broken_rules: List[BrokenRule] = []

    def add_broken(self, start_module: Module, end_module: Module, line: int):
        self.broken_rules.append(
            BrokenRule(
                start_module,
                end_module,
                line,
            )
        )
