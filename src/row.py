import json
class Row:
	def __init__(self, row_number, cells=[]):
		self.row_number = row_number
		self.cells = cells
	
	def toJSON(self):
		return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

class RowList:
	'This class is linkedlist representation of Rows'
	def __init__(self, rows=[]):
		if len(rows) > 0:
			#create linkedlist structure of input rows
			for row_in_list in rows:
				self.add_to_list(row_in_list)


	def __create_row_list(self, rows):
		for row_item in rows:
			if self.head is None:
				self.head = RowListItem(row_item)
			else:
				self.append_to_list(row_item)

	#NOTE : Need to think how to make this thread safe
	#Option 1 : we can create temporary copy of list and assign to original list after task is finished - Space issue
	#Option 2 : make remove_from_list, add_to_list and move_row_to_new_index method synchronize on some lock - Performance issue
	def add_to_list(self,row_item, row_index_to_add=None):
		# if new row index is less than head row index, then change head
		new_item_row_index = row_item.row_number
		if new_item_row_index < row_index:
			old_head = self.head
			new_head = RowListItem(row_item, self.head)
			self.head = new_head

		else:
			# search position to add new row
			current_row = self.head
			is_add_index_found = False

			while current_row is not None:
				next_row = current_row.next_row
				if next_row is not None :
					if is_add_index_found is True:
						# if add index found before just increment row index and row number
						next_row.row_index = next_row.row_index + 1
						next_row.row.row_number = next.row.row_number + 1

					elif new_item_row_index < next_row.row_index:
						# if next row in head element is not null and the new row item index is less than head's next row index, change head's next row
						is_add_index_found = True
						old_next_row = next_row
						#change next_row's row_index and row_number
						old_next_row.row_index = old_next_row.row_index + 1
						old_next_row.row.row_number = old_next_row.row.row_number + 1
						new_next_row = RowListItem(row_item, old_next_row)
						current_row.next_row = new_next_row
				else next_row is None:
					is_add_index_found = True
					new_next_row = RowListItem(row_item)
					current_row.next_row = new_next_row

				current_row = current_row.next_row 

	def remove_from_list(self, row_item):
		if self.head is None:
			return 
		#check if row_item to be removed is head item
		if self.head.row_index is row_item.row_index:
			new_head = self.head.next_row
			self.head = new_head
		else:
		# check element in list and remove
			current_row = self.head
			is_row_removed = False
			while current_row.next_row is not None:
				# decrement row_index and row_number as row is removed before this element
				if is_row_removed is True:
					current_row.next_row.row_index = current_row.next_row.row_index - 1
					current_row.next_row.row.row_number = current_row.next_row.row.row_number - 1

				row_index_to_match = current_row.next_row.row_index
				if row_index_to_match is row_item.row_index:
					#remove next row of current row and change next row
					if current_row.next_row.next_row is not None
						new_next_row = current_row.next_row.next_row
						current_row.next_row = new_next_row
					else:
						current_row.next_row = None
					is_row_removed = True

				current_row = current_row.next_row

	def move_row_to_new_index(self, row_item_to_move, to_row_index=None):
		#first remove row_item_to_move
		self.remove_from_list(row_item_to_move)
		if to_row_index is None:
			self.add_to_list(row_item_to_move)
		else:
			#change row number to next index
			row_item_to_move.row.row_number = to_row_index
			self.add_to_list(row_item_to_move)

class RowListItem:
	'This is row list item class, wrapper around row'
	def __init__(self, row, next_row=None):
		self.row = row
		self.row_index = row.row_number
		self.next_row = next_row