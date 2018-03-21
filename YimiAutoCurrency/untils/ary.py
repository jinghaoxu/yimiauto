"""
1. selenium浏览器各种操作
2. 创建人：徐敬浩
3. 创建时间：2017-11-11
"""
from selenium import webdriver
# import datetime
import time
import logging
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
# from selenium.webdriver.common.keys import Keys
from pymouse import PyMouse
# import sys
from YimiAutoCurrency.untils.until_log import log_exception_exit

logger = logging.getLogger()
m = PyMouse()


class Ary(object):
    def __init__(self, browser='chrome'):
        try:
            if browser.upper() == 'CHROME':
                driver = webdriver.Chrome()
                driver.implicitly_wait(5)  # 隐式等待
            else:
                driver = False
            self.driver = driver
            self.url = driver.current_url
            self.driver.maximize_window()
            logger.info('打开浏览器成功')
        except:
            log_exception_exit('打开浏览器错误')

    def back(self):
        self.driver.back()

    def forward(self):
        self.driver.forward()

    def refresh(self):
        self.driver.refresh()

    def element_wait(self, xpath):
        time.sleep(0.3)
        WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_all_elements_located((By.XPATH, xpath)))

    def get_element(self, xpath, css="xpath"):
        try:
            self.element_wait(xpath)
            if css == "xpath":
                element = self.driver.find_element_by_xpath(xpath)
            elif css == "id":
                element = self.driver.find_element_by_id(xpath)
            elif css == "selector":
                element = self.driver.find_element_by_css_selector(xpath)
            else:
                element = self.driver.find_elements_by_partial_link_text(xpath)
            return element
        except BaseException:
            log_exception_exit('定位不到元素：' + xpath)

    def get_elements(self, xpath, css="xpath"):
        try:
            self.element_wait(xpath)
            if css == "xpath":
                element = self.driver.find_elements_by_xpath(xpath)
            elif css == "id":
                element = self.driver.find_elements_by_id(xpath)
            elif css == "selector":
                element = self.driver.find_elements_by_css_selector(xpath)
            else:
                element = self.driver.find_elements_by_partial_link_text(xpath)
            return element
        except BaseException:
            log_exception_exit('定位不到元素：' + xpath)

    def open(self, url='http://mis.1mifudao.com/'):
        """
        1.打开一个网址
        2.例子： driver.open("https://www.baidu.com")
        """
        try:
            self.driver.get(url)
        except BaseException:
            log_exception_exit('打开url错误')
        time.sleep(0.5)

    def max_window(self):
        """
        1.使当前窗口最大化
        2.例子： driver.max_window()
        """
        self.driver.maximize_window()

    def type(self, text, xpath, css="xpath"):
        """
        1.在一个元素里输入字符
        2.例子： driver.type("sss",".//*[@id='kw']")
        3、也可以按键
        """
        self.get_element(xpath, css).send_keys(text)

    def clear(self, xpath, css="xpath"):
        """
        1.将一个元素清空
        2.例子：driver.clear(".//*[@id='kw']")
        """
        self.get_element(xpath, css).clear()

    def click(self, xpath, css="xpath"):
        """
        1.点击一个元素
        2.例子：driver.click(".//*[@id='su']")
        """
        try:
            self.get_element(xpath, css).click()
        except:
            log_exception_exit('无法点击元素：' + xpath)

    def right_click(self, xpath, css="xpath"):
        """
        1.右键点击一个元素
        2.例子：driver.right_click(".//*[@id='su']")
        """
        el = self.get_element(xpath, css)
        ActionChains(self.driver).context_click(el).perform()

    def move_to_element(self, xpath, css="xpath"):
        """
        1.鼠标移动到一个元素上
        2.例子：driver.move_to_element(".//*[@id='su']")
        """
        el = self.get_element(xpath, css)
        m.move(0, 0)
        ActionChains(self.driver).move_to_element(el).perform()

    def click_and_hold(self, xpath, css="xpath"):
        """
        1.鼠标移动到一个元素上按住
        2.例子：driver.move_to_element(".//*[@id='su']")
        """
        el = self.get_element(xpath, css)
        m.move(0, 0)
        ActionChains(self.driver).click_and_hold(el).perform()

    def double_click(self, xpath, css="xpath"):
        """
        1.双击一个元素
        2.例子：driver.double_click(".//*[@id='su']")
        """
        el = self.get_element(xpath, css)
        ActionChains(self.driver).double_click(el).perform()

    def drag_and_drop(self, star, over, css="xpath"):
        """
        1.拖动一个元素到另一个元素
        2.例子：driver.drag_and_drop(".//*[@id='su']",".//*[@id='kw']")
        """
        el = self.get_element(star, css)
        tar = self.get_element(over, css)
        m.move(0, 0)
        ActionChains(self.driver).drag_and_drop(el, tar).perform()

    def quit(self):
        """
        1.关闭浏览器
        2.driver.quit()
        """
        self.driver.quit()

    def js(self, script):
        """
        1.执行js语句
        2.driver.js(js)
        """
        self.driver.execute_script(script)
        time.sleep(0.5)

    def attr(self, xpath, attr, css="xpath"):
        """
        1.返回相应元素的某种属性
        2.driver.attr(".//p",text)
        """
        el = self.get_element(xpath, css)
        time.sleep(0.1)
        return el.get_attribute(attr)

    def switch_to_frame(self, xpath, css="xpath", index=0):
        """
        1、进入1个frame里面
        """
        el = self.get_elements(xpath, css)
        self.driver.switch_to.frame(el[index])

    def switch_to_frame_out(self):
        """
        1、退出当前frame
        """
        self.driver.switch_to.default_content()

    def alert(self, common="text"):
        """
        1、获得当前弹窗信息或者操作
        :param common: text-获得弹窗文本，accept-点击确定按钮，dismiss-点击取消按钮
        :return:
        """
        try:
            al = Alert(self.driver)
        except:
            time.sleep(0.5)
            al = Alert(self.driver)
        try:
            if common == "text":
                return al.text
            elif common == "accept":
                Alert(self.driver).accept()
            elif common == 'dismiss':
                Alert(self.driver).dismiss()
            else:
                pass
        except BaseException:
            log_exception_exit('没有找到弹窗')


if __name__ == '__main__':
    m.move(0, 0)
