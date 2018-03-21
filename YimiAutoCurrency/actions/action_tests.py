"""
1、获得用例集里面的信息
"""
from YimiAutoCurrency.constants import object_path
from YimiAutoCurrency.untils import until_excel
from YimiAutoCurrency.constants.global_variable import GLOBAL_VAR

"""
1/获取用例集信息
"""


def get_tests_info():
    testsdata = until_excel.MyExcle(object_path.TESTSPATH, object_path.TESTSHEETNAME)
    # 获得执行的用例：枚举：Y y N n
    all_data = testsdata.all_dict
    yes_data = []
    for i in all_data:
        if all_data[i]['是否运行'].upper() == 'Y':
            yes_data.append(all_data[i])
    return yes_data


"""
2/获取测试相关数据
"""


def get_test_data_info():
    test_data_info = until_excel.MyExcle(object_path.TESTDATAPATH, object_path.TESTDATASHEETNAME)
    for data in test_data_info.all_list:
        GLOBAL_VAR[data['数据名']] = data['数据']


"""
3/根据用例集信息获取用例信息
"""


def get_test_info(testinfo):
    exceldata = until_excel.MyExcle(object_path.TESTPATH % testinfo['用例文件名'], testinfo['用例工作表名'])
    return exceldata.all_dict


if __name__ == '__main__':
    print(get_test_data_info())
