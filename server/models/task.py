import json

class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description

    def __repr__ (self) -> str:
        obj = {
            "title": self.title,
            "description": self.description
        }
        return json.dumps(obj)