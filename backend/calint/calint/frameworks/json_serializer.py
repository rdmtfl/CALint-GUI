from os import stat
from typing import Dict
import json
from calint.adapters import SerializerAdapter


class JsonSerializer(SerializerAdapter):
    @staticmethod
    def serialize(data: Dict) -> str:
        return json.dumps(data)

    @staticmethod
    def deserialize(source: str) -> Dict:
        return json.loads(source)
