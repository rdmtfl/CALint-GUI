from dataclasses import dataclass


@dataclass
class Layer:
    priority: int
    import_path: str
    name: str
