from typing import List

from .module import Module
from .layer import Layer


class LocalConfig:
    def __init__(self, roots: List[str]) -> None:
        self.layers: List[Layer] = []
        self.roots = roots

    def add_layer(self, layer: Layer):
        self.layers.append(layer)

    def sort_layers(self) -> List[Layer]:
        self.layers = sorted(self.layers, key=lambda x: x.priority)
        return self.layers

    def find_layer(self, module: Module) -> Layer:
        return next(x for x in self.layers if x.import_path in module.path)
