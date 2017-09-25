# coding=utf-8
import xlrd


class FileProcessor:

    def __init__(self, file_path):
        self.file_path = file_path
        try:
            self.file = xlrd.open_workbook(self.file_path, encoding_override='utf-8')
            self.sheet = self.file.sheet_by_index(0)  # default number : 0
            self.value_dict = dict()
        except Exception, e:
            print str(e)

    def data_exist(self):
        if self.sheet.ncols <= 0 or self.sheet.nrows <= 0:
            return False
        return True

    def parse_sheet(self):
        name_col = self.sheet.col_values(0)
        id_col = self.sheet.col_values(1)

        for i in range(len(name_col)):
            self.value_dict[name_col[i]] = id_col[i]

        return self.value_dict

