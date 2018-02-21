import json
import workbook
import worksheet
import cell
import row

def deserialize_workbook(jsonData):
    try:
        decoded = json.loads(jsonData)
        workbook_name = decoded['workbook_name']
        worksheets = []
        for ws in decoded['worksheets']:
            worksheet_name = ws['worksheet_name']
            rows = []
            for jsonrow in ws['rows']:
                row_number = jsonrow['row_number']
                cells = []
                for cl in jsonrow['cells']:
                    column_number = cl['column_number']
                    cellcontent_type = cl['cell_content']['cell_type']
                    value = None
                    c_formula = None
                    print('cell_type : ' + str(cellcontent_type))
                    if cellcontent_type is cell.CellContent.CELL_TYPE_VALUE:
                        value = cl['cell_content']['value']

                    elif cellcontent_type is cell.CellContent.CELL_TYPE_FORMULA:
                        formula_type = cl['cell_content']['formula']['type']
                        operands = []
                        for operand in cl['cell_content']['formula']['operands']:
                            operands.append(operand)
                        c_formula = get_fomula_object(formula_type, operands)
                    else:
                        #REMOVE
                        print('invalid content type')
                        pass

                    cell_content = cell.CellContent(value, c_formula)
                    c_cell = cell.Cell(column_number, cell_content)
                    cells.append(c_cell)
                c_row = row.Row(row_number, cells)
                rows.append(c_row) 
            c_worksheet = worksheet.Worksheet(worksheet_name, rows)
            worksheets.append(c_worksheet)
        wb = workbook.Workbook(workbook_name, worksheets)
        return wb
    except (ValueError, KeyError, TypeError) as e:
        print(e)
        print ("JSON format error")

def get_fomula_object(formula_type, operands):
    cell_formula = None
    if formula_type == 1:
        cell_formula = cell.SumFormula(operands)
        cell_formula.type = formula_type
    elif formula_type == 2:
        cell_formula = cell.DivideFormula(operands)
        cell_formula.type = formula_type
    elif formula_type == 3:
        cell_formula = cell.MultiplyFormula(operands)
        cell_formula.type = formula_type
    elif formula_type == 4:
        cell_formula = cell.SubtractFormula(operands)
        cell_formula.type = formula_type
    else:
        cell_formula = cell.AverageFormula(operands)
        cell_formula.type = formula_type
    return cell_formula