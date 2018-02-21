import json
import row

class Worksheet:
    'Base class for worksheet.'
    def __init__(self, worksheet_name, rows={}):
        self.worksheet_name = worksheet_name
        self.rows = rows

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

class WorksheetProcessor:
	'worksheet processor class to add, remove or move rows'
	def __init__(self, worksheet):
		self.worksheet_to_process = worksheet
		#assign length of rows dictonary to next_row_number
        self._next_row_number = len(self.worksheet_to_process.rows)
        self._next_row_number+= 1
        self.rows_list = row.RowList(self.worksheet_to_process.rows)

	def add_row(self, new_row=None):
    	#increment next row number in self object
    	if new_row is not None:
    		return self.__append_new_row_to_list(new_row)
    	else:
    		#create new row with next row_number
    		return self.__append_new_row_to_list(self)

    def remove_row(self, row):
    	#decrement next row number in self object
    	self.rows_list.remove_from_list(row)
    	self._next_row_number -= 1
    	self.worksheet_to_process.rows.remove(row)

    def move_row(self, row_item_to_move, to_index = None):
    	self.rows_list.move_row_to_new_index(row_item_to_move, to_index)
 	
 	def __create_and_append_new_row_to_list(self):
    	new_row_to_be_appended = row.Row(self._next_row_number)
		self.rows_list.add_to_list(new_row_to_be_appended, new_row_to_be_appended.row_number)
		self._next_row_number += 1
		self.worksheet_to_process.rows.append(new_row_to_be_appended)
		return new_row_to_be_appended

	def __append_new_row_to_list(self, new_row):
		#get row_number
		self.rows_list.add_to_list(new_row, new_row.row_number)
		self._next_row_number += 1
		self.worksheet_to_process.rows.append(new_row)
		return new_row