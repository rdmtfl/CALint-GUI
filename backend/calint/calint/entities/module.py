from dataclasses import dataclass

from .layer import Layer


@dataclass
class Module:
    path: str
    layer: Layer
