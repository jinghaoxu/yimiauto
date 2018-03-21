"""
1. 创建人：徐敬浩
2. 创建时间：2017-11-28
3. 关于Excel文件的操作
4. 读取一个Excel文件的某一个表的数据
"""
import xlrd
import xlwt
import logging

logger = logging.getLogger()

"""
参数说明：
1、self.sheet_names：该文件所有的工作表的名称
2、self.ncols：该表的列数
3、self.nrows：该表的行数
4、self.frist_row_data：第一行数据
5、self.all_list：所有数据：以第一行数据为键，后面的数据为值，值为列表
6、self.all_dict：所有数据：以第一行数据为键，后面的数据为值，值为字典，键为行数，值为每一行的数据
该类有两个参数，文件路径和工作表名称
例子：
data = MyExcle('D:/yimi_work/yimi_auto_test_001/data/test_001test_001.xlsx', 'Sheet1')
print(data.all_list)
"""


class MyExcle(object):
    def __init__(self, path, sheet_name):
        # 获得表对象
        object_data = xlrd.open_workbook(path)

        self.sheet_names = object_data.sheet_names()

        sheet = object_data.sheet_by_name(sheet_name)
        self.ncols = sheet.ncols  # 该表的列数
        self.nrows = sheet.nrows  # 该表的行数
        self.frist_row_data = []
        self.all_list = []
        self.all_dict = {}
        # 生成第一行数据
        for col in range(0, self.ncols):
            self.frist_row_data.append(sheet.cell_value(0, col))

        # 生成所有数据：以第一行数据为键，后面的数据为值
        row_data = {}
        for row in range(1, self.nrows):
            for col in range(0, self.ncols):
                con_data = sheet.cell_value(row, col)
                if isinstance(con_data, float):
                    if con_data == int(con_data):
                        con_data = str(int(con_data))
                    else:
                        pass
                else:
                    pass
                row_data[str(self.frist_row_data[col])] = con_data
            # row_data['行数'] = row
            # 注意 = 和 copy()的区别
            self.all_list.append(row_data.copy())
            self.all_dict[str(row)] = row_data.copy()


# def strcol(self,colname):
# 	"""
# 	将某一列全部置换为整数
# 	:param colname: 列名
# 	:return: null
# 	"""
# 	for i in self.all_dict:
# 		date = self.all_dict[i][colname]
# 		if isinstance(date, (int,float)):
# 			self.all_dict[i][colname] = str(int(date))
# 		else:
# 			pass


# 生成测试报告
class NewExcel(object):

    def __init__(self):
        self.row = 0

        self.workbook = xlwt.Workbook()
        self.ws = self.workbook.add_sheet('测试报告')
        self.add_row('用例编号', '用例结果')

    def add_row(self, value1, value2):
        self.ws.write(self.row, 0, value1)
        self.ws.write(self.row, 1, value2)
        self.row = self.row + 1

    def save(self, path, name):
        self.workbook.save(str(path) + '/' + str(name) + '.xlsx')


if __name__ == '__main__':
    a = NewExcel()
    a.save('./a', '11')
