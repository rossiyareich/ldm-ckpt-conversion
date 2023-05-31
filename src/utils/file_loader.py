import json

class file_loader:
    def load_json(self, filepath):
        with open(filepath, "r") as f:
            j = json.load(f)

        return j