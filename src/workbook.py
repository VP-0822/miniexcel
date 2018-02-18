import json
import worksheet

class Workbook:
    'workbook base class'

    def __init__(self, workbook_name, worksheets):
        self.workbook_name = workbook_name
        self.worksheets = worksheets

    def add_worksheet(self, worksheet_name='sheet 1'):
        new_worksheet = worksheet.Worksheet(worksheet_name)
        self.worksheets.append(new_worksheet)

    def remove_worksheet(self, worksheet_name):
        for ws in self.worksheets:
            if ws.worksheet_name == worksheet_name:
                self.worksheets.remove(ws)
    


    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)