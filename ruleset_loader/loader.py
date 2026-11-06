import json
from pathlib import Path
from .registry import RulesetRegistry

class RulesetLoader:
    def __init__(self):
        self.registry=RulesetRegistry()

    def load(self,path):
        data=json.loads(Path(path).read_text(encoding="utf-8"))
        self.registry.register(data)
        return data

    def load_directory(self,root):
        for p in Path(root).rglob("*.json"):
            self.load(p)
        return self.registry
