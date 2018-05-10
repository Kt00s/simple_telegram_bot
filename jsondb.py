"""
this module simplifies work with .json files
"""
import json


class JsonDB:
    def __init__(self, file_path: str):
        self.file_path = file_path
        with open(file_path, "r", encoding="utf-8") as file:
            self.dictionary = json.loads(file.read())

    def write(self):
        with open(self.file_path, "w", encoding="utf-8") as file:
            file.write(json.dumps(self.dictionary, ensure_ascii=False))
