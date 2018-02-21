import json

class Cell:
    'Base class for cell in worksheet.'

    def __init__(self, column_number, cell_content=None):
        self.column_number = column_number
        self.cell_content = cell_content

    def __is_alphabet(self, character):
        return str(character).isalpha()

    def __is_digit(self, character):
        return str(character).isdigit()

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

class CellContent:
    'This class represents cell content.'
    CELL_TYPE_VALUE = 1
    CELL_TYPE_FORMULA = 2
    CELL_TYPE_INVALID = -1

    def __init__(self, value=None, formula=None):
        self.value = value
        self.formula = formula

        if self.value is not None:
            self.cell_type = CellContent.CELL_TYPE_VALUE
        elif self.formula is not None:
            self.cell_type = CellContent.CELL_TYPE_FORMULA
        else:
            self.cell_type = CellContent.CELL_TYPE_INVALID

    def get_display_value(self):
        if self.cell_type == CellContent.CELL_TYPE_INVALID:
            #throw error for invalid cell content
            return -1
        elif self.cell_type == CellContent.CELL_TYPE_VALUE:
            return self.value
        else:
            return self.__calculate_formula_value()

    def __calculate_formula_value(self):
        if type(self.formula) is not CellFormula:
            #TODO : throw exception
            return -1
        return CellFormula(self.formula).calculate_value()

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

class CellFormula:
    'This class represents cell formula.'

    def __init__(self, operands, type):
        self.operands = operands
        self.type = type

    def calculate_value(self):
        return None

    def get_operand_values(self, operand):
        operand_values = []
        if type(operand) is int or type(operand) is float:
            operand_values.append(operand)
            return operand_values

        elif type(operand) is str:
            #if cell range is provided
            if ':' in operand:
                range_values = str(operand).split(':')
                start_position =  range_values[0]
                end_position = range_values[1]

                #TODO : call utility to get cell for cell reference like C1
                #append value in operand_values
            else:
                #TODO : call utility to get cell for cell reference
                #append value in operand_values
                #REMOVE
                return -1
        else:
            #TODO : throw error, invalid value in formula
            # REMOVE
            return -1
        return operand_values

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

class SumFormula(CellFormula):
    'This class represents Sum Formula.'

    def __init__(self, operands):
        super().__init__(operands,1)

    def calculate_value(self):
        return_value = 0.0
        for operand in self.operands:
            operand_values = self.get_operand_values(operand)
            for value in operand_values:
                return_value += value
        return return_value

class DivideFormula(CellFormula):
    'This class represents Divide Formula.'

    def __init__(self, operands):
        super().__init__(operands,2)

    def calculate_value(self):
        return_value = 0.0
        for operand in self.operands:
            operand_values = self.get_operand_values(operand)
            for value in operand_values:
                return_value /= value
        return return_value

class MultiplyFormula(CellFormula):
    'This class represents Multiply Formula.'

    def __init__(self, operands):
        super().__init__(operands,3)

    def calculate_value(self):
        return_value = 0.0
        for operand in self.operands:
            operand_values = self.get_operand_values(operand)
            for value in operand_values:
                return_value *= value
        return return_value

class SubtractFormula(CellFormula):
    'This class represents Subtract Formula.'

    def __init__(self, operands):
        super().__init__(operands,4)

    def calculate_value(self):
        return_value = 0.0
        for operand in self.operands:
            operand_values = self.get_operand_values(operand)
            for value in operand_values:
                return_value -= value
        return return_value

class AverageFormula(CellFormula):
    'This class represents Average Formula.'

    def __init__(self, operands):
        super().__init__(operands,5)

    def calculate_value(self):
        return_value = 0.0
        number_of_operands = 0
        for operand in self.operands:
            operand_values = self.get_operand_values(operand)
            for value in operand_values:
                return_value -= value
                number_of_operands += 1
        return return_value/number_of_operands

if __name__ == '__main__' :
    sumFor = SumFormula([5,6])
    cellCon = CellContent(formula=sumFor)
    lcell = Cell('A21', cellCon)
    jsonData = lcell.toJSON()
    print(jsonData)

    jsonObject = json.loads(jsonData, object_hook=Cell)

    print(jsonObject.__dict__)