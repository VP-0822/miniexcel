import json
import JSONDeserializer
import cell
import worksheet
import workbook

sumFor = cell.SumFormula([5,6])
cellCon = cell.CellContent(formula=sumFor)
lsumcell = cell.Cell('A1', cellCon)

mulFor = cell.MultiplyFormula([2*1])
mulCellCon = cell.CellContent(formula=mulFor)
lmulcell = cell.Cell('A2', mulCellCon)

worksheet1 = worksheet.Worksheet('somedata', [lsumcell,lmulcell])

sumFor1 = cell.SumFormula([5,6])
cellCon1 = cell.CellContent(formula=sumFor1)
lsumcell1 = cell.Cell('A1', cellCon1)

mulFor1 = cell.MultiplyFormula([2*1])
mulCellCon1 = cell.CellContent(formula=mulFor1)
lmulcell1 = cell.Cell('A2', mulCellCon1)

worksheet2 = worksheet.Worksheet('anotherdatasheet', [lsumcell1, lmulcell1])

workbook = workbook.Workbook('testbook', [worksheet1, worksheet2])

samplejsondata = workbook.toJSON()

#print(samplejsondata)

data = JSONDeserializer.deserialize_workbook(samplejsondata)
print(data.worksheets[0].cells[0].row_number)
print(data.worksheets[0].cells[0].column_number)
print(data.worksheets[0].cells[0].cell_content.formula)
print(data.worksheets[0].cells[0].cell_content.formula.operands)