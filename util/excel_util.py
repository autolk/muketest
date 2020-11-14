import xlrd
import time
class ExcelUtil(object):
    def __init__(self,excel_path=None,index=None):
        if excel_path == None:
            self.excel_path = 'C:/Users/Administrator/Desktop/hexin/data/logindata.xls'
        else:
            self.excel_path = excel_path
        if index == None:
            index = 0
        self.data = xlrd.open_workbook(self.excel_path)
        self.table = self.data.sheets()[index]
    def get_data(self):
        result = []
        rows = self.get_lines()
        if rows !=None:
            for i in range(rows):
                col = self.table.row_values(i)
                result.append(col)
            return result
        return None

    def get_lines(self):
        rows = self.table.nrows
        if rows >= 1:
            return rows
        return None

if __name__ == '__main__':
    excel_path = 'C:/Users/Administrator/Desktop/hexin/data/logindata.xls'
    excel_util = ExcelUtil(excel_path)
    data = excel_util.get_data()[0]
    username, password = data
    print(username,password)

