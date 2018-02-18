import json

class Workbook:
    'workbook base class'

    def __init__(self, workbook_name, worksheets):
        self.workbook_name = workbook_name
        self.worksheets = worksheets

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)