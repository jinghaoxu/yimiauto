from YimiAutoCurrency.untils import until_sqllite3 as us
from YimiDjango.ussd.case import caseRm
from YimiDjango.ussd.case import caseWm
from YimiDjango.ussd.until import data_handle

'''
用例页面数据处理
'''
# 全局变量
get_case_select_data = ''


# 用例页面 查询列表基础数据
def get_case_select(data):
    global get_case_select_data
    get_case_select_data = ''
    # 参数处理
    param = []
    suiteid, param = data_handle.isnull(data, 'suiteid', param)
    modularid, param = data_handle.isnull(data, 'modularid', param)
    casename, param = data_handle.isnull(data, 'casename', param)

    def add(name):
        global get_case_select_data
        get_case_select_data += caseRm.select[name]

    def addif(idd, name):
        global get_case_select_data
        get_case_select_data += data_handle.addif(idd, caseRm.select[name])

    # sql拼接
    add('base1')
    addif(suiteid, 'suite1')
    add('base2')
    addif(casename, 'casename1')
    addif(suiteid, 'suite2')
    addif(modularid, 'modularid1')
    add('end')
    return us.sqlite_select(get_case_select_data, param)
