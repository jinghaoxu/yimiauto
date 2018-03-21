import os

# 项目地址：D:/yimi_work/yimi_auto_test_001
OBJECTPATH = os.path.dirname(os.path.dirname(__file__))

# 用例集地址：
TESTSPATH = OBJECTPATH + '/data/测试用例集.xlsx'
TESTSHEETNAME = 'main'

# 用例地址
TESTPATH = OBJECTPATH + '/data/Keywords/%s.xlsx'

# 用例相关数据地址：
TESTDATAPATH = OBJECTPATH + '/data/测试相关数据.xlsx'
TESTDATASHEETNAME = 'main'
