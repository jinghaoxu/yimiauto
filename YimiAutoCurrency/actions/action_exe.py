from time import sleep
from YimiAutoCurrency.constants.function_list import FUNLIST
from YimiAutoCurrency.constants.function_list import PARPROLIST
from YimiAutoCurrency.constants.global_variable import GLOBAL_VAR
import logging
from YimiAutoCurrency.untils import until_md5
from YimiAutoCurrency.untils import until_screen_shot

logger = logging.getLogger()

"""
对于操作数据的处理：去除空格，转换数据
"""


def data_process(data):
    data = str(data).strip()  # 去除空格
    data = FUNLIST[data]
    return data


"""
对于获得的单条用例数据，进行处理
"""


def execute_one_test(driver, test_list):
    flag = 2  # 0:失败， 1：成功， 2：不生成报告
    exe_types = data_process(test_list['操作类型'])
    exe_type_css = exe_types.split('_')[-1]
    if exe_type_css == 'id' or exe_type_css == 'selector' or exe_type_css == 'xpath':
        exe_type = exe_types.rstrip(exe_type_css).rstrip('_')
    else:
        exe_type = exe_types

    attr_value = str(test_list['元素属性值']).strip()
    parameter = str(test_list['参数值']).strip()

    if str(test_list['参数处理']).strip().__len__() > 0:
        parameter_handle = PARPROLIST[str(test_list['参数处理']).strip()]
    else:
        parameter_handle = str(test_list['参数处理']).strip()

    assert_result = str(test_list['检查点预期结果']).strip()

    # 参数处理
    if parameter_handle == 'MD5':
        parameter = until_md5.md5(parameter)
    elif parameter_handle == 'var':
        parameter = GLOBAL_VAR[parameter]
    else:
        pass

    # 执行用例
    if exe_type == 'open':
        driver.open(attr_value)

    elif exe_type == 'back':
        driver.back()

    elif exe_type == 'forward':
        driver.forward()

    elif exe_type == 'refresh':
        driver.refresh()

    elif exe_type == 'max':
        driver.max_window()

    elif exe_type == 'quit':
        driver.quit()

    elif exe_type == 'get_alert_text':
        GLOBAL_VAR[parameter.upper()] = driver.alert('text')
        logger.info('生成变量：' + parameter + ': ' + GLOBAL_VAR[parameter.upper()])

    elif exe_type == 'alert_accept':
        driver.alert('accept')

    elif exe_type == 'alert_dismiss':
        driver.alert('dismiss')

    elif exe_type == 'sleep':
        sleep(float(parameter) / 1000)

    elif exe_type == 'click':
        driver.click(attr_value, css=exe_type_css)

    elif exe_type == 'type':
        driver.type(parameter, attr_value, css=exe_type_css)

    elif exe_type == 'clear':
        driver.clear(attr_value, css=exe_type_css)

    elif exe_type == 'right_click':
        driver.right_click(attr_value, css=exe_type_css)

    elif exe_type == 'move':
        driver.move_to_element(attr_value, css=exe_type_css)

    elif exe_type == 'move_hold':
        driver.click_and_hold(attr_value, css=exe_type_css)

    elif exe_type == 'drag_and_drop':
        driver.drag_and_drop(attr_value, parameter, css=exe_type_css)

    elif exe_type == 'exe_js':
        driver.js(parameter)

    elif exe_type == 'in_frame':
        driver.switch_to_frame(attr_value, css=exe_type_css)

    elif exe_type == 'out_frame':
        driver.switch_to_frame_out()

    elif exe_type == 'get_text':
        GLOBAL_VAR[parameter.upper()] = driver.attr(attr_value, 'text', css=exe_type_css)
        logger.info('生成变量：' + parameter + ': ' + GLOBAL_VAR[parameter.upper()])

    elif exe_type == 'get_attr':
        GLOBAL_VAR[parameter.upper()] = driver.attr(attr_value, assert_result, css=exe_type_css)
        logger.info('生成变量：' + parameter + ': ' + GLOBAL_VAR[parameter.upper()])

    elif exe_type == 'assert_test_agreement':
        text = driver.attr(attr_value, 'text', css=exe_type_css)
        try:
            assert text == assert_result
            flag = 1
        except AssertionError:
            flag = 0
            logger.exception('断言失败 - 实际结果：' + str(text) + '  用例数据：' + str(test_list))
            until_screen_shot.pngshot('assert_error')

    elif exe_type == 'assert_attr_agreement':
        data = driver.attr(attr_value, parameter, css=exe_type_css)
        try:
            assert data == assert_result
            flag = 1
        except AssertionError:
            flag = 0
            logger.exception('断言失败 - 实际结果：' + str(data) + '  用例数据：' + str(test_list))
            until_screen_shot.pngshot('assert_error')

    elif exe_type == 'assert_var_agreement':
        data = GLOBAL_VAR[parameter.upper()]
        try:
            assert data == assert_result
            flag = 1
        except AssertionError:
            flag = 0
            logger.exception('断言失败 - 实际结果：' + str(data) + '  用例数据：' + str(test_list))
            until_screen_shot.pngshot('assert_error')

    elif exe_type == 'assert_test_contain':
        data = driver.attr(attr_value, 'test', css=exe_type_css)
        try:
            assert assert_result in data
            flag = 1
        except AssertionError:
            flag = 0
            logger.exception('断言失败 - 实际结果：' + str(data) + '  用例数据：' + str(test_list))
            until_screen_shot.pngshot('assert_error')

    elif exe_type == 'assert_attr_contain':
        data = driver.attr(attr_value, parameter, css=exe_type_css)
        try:
            assert assert_result in data
            flag = 1
        except AssertionError:
            flag = 0
            logger.exception('断言失败 - 实际结果：' + str(data) + '  用例数据：' + str(test_list))
            until_screen_shot.pngshot('assert_error')

    elif exe_type == 'assert_var_contain':
        data = GLOBAL_VAR[parameter.upper()]
        try:
            assert assert_result in data
            flag = 1
        except AssertionError:
            flag = 0
            logger.exception('断言失败 - 实际结果：' + str(data) + '  用例数据：' + str(test_list))
            until_screen_shot.pngshot('assert_error')

    elif exe_type == 'print':
        print(GLOBAL_VAR[parameter.upper()])

    else:
        print(exe_type + ':error 无相应的操作类型')
        pass

    return flag
