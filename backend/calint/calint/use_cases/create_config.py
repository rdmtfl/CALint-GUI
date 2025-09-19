from typing import Dict
from calint.entities import LocalConfig, Layer
from calint.use_cases.ports import CreateConfigPort


def create_config(input: CreateConfigPort, input_source: str) -> LocalConfig:
    with open(input_source) as local_config_file:
        deserialized_config: Dict = input.get_config_input(local_config_file)

    roots = deserialized_config.pop("roots")
    local_config = LocalConfig(roots)

    for name, layer in deserialized_config.items():
        local_config.add_layer(Layer(layer[1], layer[0], name))

    return local_config
