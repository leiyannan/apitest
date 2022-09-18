import openpyxl

class ExcelHandler:

    def __init__(self, file_path):
        """初始化"""
        self.file_path = file_path
        self.worbook = None

    def open_file(self):
        """打开文件"""
        workbook = openpyxl.load_workbook(self.file_path)
        self.worbook = workbook
        return workbook


    def get_sheet(self, name):
        """获取表格"""
        workbook = self.open_file()
        return workbook[name]

    def read_data(self,name):
        """读取数据：每一行数据存放到列表或字典当中"""
        sheet = self.get_sheet(name)
        # 获取所有行
        rows = list(sheet.rows)
        data = []
        # 获取标题
        headers = []
        for title in rows[0]:
            headers.append(title.value)

        # 添加数据
        for row in rows[1:]:
            row_data = {}
            for idx, cell in enumerate(row):
                row_data[headers[idx]] = cell.value
            data.append(row_data)
        return data

    def write(self, sheet_name,row,column,data):
        """写入单元格数据"""
        sheet = self.get_sheet(sheet_name)
        sheet.cell(row,column).value = data
        self.save()
        self.worbook.close()

    def save(self):
        """保存文件"""
        self.worbook.save(self.file_path)


    def close(self):
        self.worbook.close()

if __name__ == '__main__':
    pass


