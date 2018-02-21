import JSONDeserializer
import workbook

class WorkbookHandler:
    'This class handles workbook opening/closing jobs.'

    #dictionary to maintain opened workbooks against thier file paths  
    opened_workbooks = {}
    
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
        self.opened_workbooks[self.workbook_file_path] = self.workbook

    def write_workbook_data(self, workbook_file_path=None):
        #write workbook data into JSON file
        if workbook_file_path is not None
            self.workbook_file_path = workbook_file_path
        workbook_json_data = self.workbook.toJSON()
        workbook_file = open(self.workbook_file_path, 'w')
        workbook_file.write(workbook_json_data)
        workbook_file.close()
        self.opened_workbooks[self.workbook_file_path] = self.workbook

    def close_workbook(self, save_and_close=True):
        if save_and_close == False:
            del self.opened_workbooks[self.workbook_file_path]
        else:
            self.write_workbook_data()
            del self.opened_workbooks[self.workbook_file_path]

    def get_all_opened_workbooks(self):
        return self.opened_workbooks.values()

    def get_workbook_processor(self, workbook_file_path=None, workbook=None):
        if workbook is not None:
            return self.__get_workbook_processor_inner(workbook)
        elif workbook_file_path is not None:
            return self.__get_workbook_processor_for_filepath(workbook_file_path)
        else:
            return None
            
    def __get_workbook_processor_inner(self, workbook):
        return self.opened_workbooks[workbook.workbook_file_path]

    def __get_workbook_processor_for_filepath(self, workbook_file_path):
        return self.opened_workbooks[workbook_file_path]