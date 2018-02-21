import json
import JSONDeserializer
import cell
import worksheet
import workbook
import row


sumFor = cell.SumFormula([5,6])
cellCon = cell.CellContent(formula=sumFor)
lsumcell = cell.Cell('A', cellCon)

mulFor = cell.MultiplyFormula([2*1])
mulCellCon = cell.CellContent(formula=mulFor)
lmulcell = cell.Cell('A', mulCellCon)

row_1 = row.Row('1',[lsumcell,lmulcell])

sumForr2 = cell.SumFormula([5,6])
cellConr2 = cell.CellContent(formula=sumForr2)
lsumcellr2 = cell.Cell('A', cellConr2)

mulForr2 = cell.MultiplyFormula([2*1])
mulCellConr2 = cell.CellContent(formula=mulForr2)
lmulcellr2 = cell.Cell('A', mulCellConr2)

row_2 = row.Row('2',[lsumcellr2,lmulcellr2])

worksheet1 = worksheet.Worksheet('somedata', [row_1,row_2])

sumFor3 = cell.SumFormula([5,6])
cellCon3 = cell.CellContent(formula=sumFor3)
lsumcell3 = cell.Cell('A', cellCon3)

mulFor3 = cell.MultiplyFormula([2,1])
mulCellCon3 = cell.CellContent(formula=mulFor3)
lmulcell3 = cell.Cell('A', mulCellCon3)

row_3 = row.Row('1', [lsumcell3, lmulcell3])

worksheet2 = worksheet.Worksheet('anotherdatasheet', [row_3])

workbook = workbook.Workbook('testbook', [worksheet1, worksheet2])

samplejsondata = workbook.toJSON()

print(samplejsondata)

data = JSONDeserializer.deserialize_workbook(samplejsondata)
#print(data.worksheets[0].cells[0].row_number)
print(data.worksheets[0].rows[0].cells[0].column_number)
print(data.worksheets[0].rows[0].cells[0].cell_content.formula)
print(data.worksheets[0].rows[0].cells[0].cell_content.formula.operands)