"""
1、主函数
2、执行函数
3、创建人：徐敬浩
4、创建时间：2017-11-28
5、运行函数
"""
from YimiAutoCurrency.untils import until_log
import logging
from YimiAutoCurrency.actions import action_tests
from YimiAutoCurrency.actions import action_exe
from YimiAutoCurrency.untils import ary
from YimiAutoCurrency.untils import until_excel
from YimiAutoCurrency.untils import until_time


# 初始化函数
def config_init():
    until_log.log_init()


# 主函数
def main():
    config_init()
    logger = logging.getLogger()
    logger.info('开始执行用例')
    driver = ary.Ary()
    # 获得用例集数据
    tests_info = action_tests.get_tests_info()
    # 获取测试相关数据，保存到变量列表里面
    action_tests.get_test_data_info()

    # 根据用例集获得用例数据
    for test_info in tests_info:
        try:
            test_result = until_excel.NewExcel()
            test_data_s = action_tests.get_test_info(test_info)
            # 根据用例数据，一条条执行用例
            for test_id in test_data_s:
                flag = action_exe.execute_one_test(driver, test_data_s[test_id])
                if flag == 2:
                    pass
                elif flag == 1:
                    test_result.add_row(int(test_id) + 1, 'Y')
                else:
                    test_result.add_row(int(test_id) + 1, 'N')

            name = test_info['用例文件名'] + ' - 测试报告 - ' + until_time.stamp()
            path = './data/TestResult'
            test_result.save(path, name)

        except:
            logger.exception('用例执行报错')
    logger.info('用例执行完毕')


if __name__ == '__main__':
    main()
