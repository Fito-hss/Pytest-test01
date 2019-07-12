# 导包
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class Base(object):
    def __init__(self):
        desired_caps = {}
        # 设备信息
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = '192.168.56.101:5554'
        # app信息
        desired_caps['appPackage'] = 'com.vcooline.aike'
        desired_caps['appActivity'] = '.umanager.LoginActivity'
        # 获取driver
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    # 查找元素
    def base_find(self,loc, timeout=30, poll=0.5):
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 输入方法
    def base_input(self,loc,text):
        element = self.base_find(loc)
        element.clear()
        element.send_keys(text)

    # 点击方法
    def base_click(self,loc):
        self.base_find(loc).click()
