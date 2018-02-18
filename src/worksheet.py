import json

class Worksheet:
    'Base class for worksheet.'
    def __init__(self, worksheet_name, cells):
        self.worksheet_name = worksheet_name
        self.cells = cells

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
