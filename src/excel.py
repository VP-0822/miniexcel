import JSONDeserializer

class WorkbookHandler:
    opened_workbooks = {}
    'This class handles workbook opening/closing jobs.'
    def __init__(self, workbook_name):
        self.workbook_name = workbook_name
        self.workbook = None

    def load_workbook_data(self, data_file_path):
        # load workbook from json file
        self.workbook_file_path = data_file_path
        workbook_file = open(data_file_path, 'r')
        workbook_json_data = workbook_file.read().replace('\n', '')
        workbook_file.close()
        self.workbook = JSONDeserializer.deserialize_workbook(workbook_json_data)
        self.opened_workbooks[self.workbook_name] = self.workbook

    def write_workbook_data(self, workbook_file_path=None):
        #write workbook data into JSON file
        if workbook_file_path is not None
            self.workbook_file_path = workbook_file_path
        workbook_json_data = self.workbook.toJSON()
        workbook_file = open(self.workbook_file_path, 'w')
        workbook_file.write(workbook_json_data)
        workbook_file.close()
        self.opened_workbooks[self.workbook_name] = self.workbook

    def close_workbook(self, save_and_close=True):
        if save_and_close == False:
            # remove workbook
            del self.opened_workbooks[self.workbook_name]
        else:
            self.write_workbook_data()
            # remove workbook
            del self.opened_workbooks[self.workbook_name]