import json
from typing import Any, Dict, List

class Processor:
    def __init__(self, data: List[Dict[str, Any]]) -> None:
        self.data = data

    def filter_data(self, criteria: Dict[str, Any]) -> List[Dict[str, Any]]:
        filtered = []
        for item in self.data:
            if all(item.get(k) == v for k, v in criteria.items()):
                filtered.append(item)
        return filtered

    def sort_data(self, key: str, reverse: bool = False) -> List[Dict[str, Any]]:
        return sorted(self.data, key=lambda x: x.get(key), reverse=reverse)

    def to_json(self) -> str:
        return json.dumps(self.data, indent=4)

    @staticmethod
    def from_json(json_string: str) -> List[Dict[str, Any]]:
        return json.loads(json_string)