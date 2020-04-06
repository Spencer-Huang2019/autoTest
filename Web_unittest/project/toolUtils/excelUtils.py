import xlrd
from xlutils.copy import copy

class excelRead(object):
    def __init__(self, filepath):
        self.filepath = filepath
        self.workBook = xlrd.open_workbook(self.filepath, formatting_info=True)

    # get sheet info as list
    def getSheetInfo(self, sheetName, cols, cole):
        workSheet = self.workBook.sheet_by_name(sheetName)
        sheetInfo = []
        nRows = workSheet.nrows
        for row in range(1, nRows):
            sheetInfo.append(tuple(workSheet.row_values(row, cols, cole)))
        return sheetInfo

class excelWrite(excelRead):

    def __init__(self, filepath):
        super().__init__(filepath)
        self.wrbook = copy(self.workBook)

    def write(self, sheetName, row, col, msg):
        wrsheet = self.wrbook.get_sheet(sheetName)
        wrsheet.write(row, col, msg)
        self.wrbook.save(self.filepath)

    def createSheet(self, newSheet):
        self.wrbook.add_sheet(newSheet)
        self.wrbook.save(self.filepath)

if __name__ == '__main__':
    filepath = r'../../documents/api_TC.xls'
    excel = excelRead(filepath)
