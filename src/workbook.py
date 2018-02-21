import json
import worksheet

class Workbook:
    'workbook base class'

    def __init__(self, workbook_name, worksheets):
        self.workbook_name = workbook_name
        self.worksheets = worksheets
    
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

class WorkbookProcessor:
	'workbook processor class to add or remove worksheets'

	def __init__(self, workbook):
		self.workbook_to_process = workbook

	def add_worksheet(self, worksheet_name='sheet 1'):
        new_worksheet = worksheet.Worksheet(worksheet_name)
        self.workbook_to_process.worksheets.append(new_worksheet)

    def remove_worksheet(self, worksheet_name):
        for ws in self.workbook_to_process.worksheets:
            if ws.worksheet_name is worksheet_name:
                self.worksheets.remove(ws)