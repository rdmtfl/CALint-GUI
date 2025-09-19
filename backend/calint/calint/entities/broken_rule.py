from dataclasses import dataclass
from .module import Module

@dataclass
class BrokenRule:
    start: Module
    end: Module
    line: int
