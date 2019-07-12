import os
import sys

from page.page_login import PageLogin
from tool.read_yaml import read

sys.path.append(os.getcwd())

import pytest



# def get_data():
#     return [('13800001111', '123456'), ('13800001112', '0000')]

def get_data():
    arrs = []
    for data in read().values():
        arrs.append((data.get('username'),data.get('pwd')))
    return arrs

class TestLogin(object):
    # 初始化
    def setup_class(self):
        # 实例化PageLogin
        self.login = PageLogin()

    # 结束
    def teardown_class(self):
        self.login.driver.quit()

    # 登录测试方法
    @pytest.mark.parametrize('phone,pwd', get_data())
    def test_login(self, phone, pwd):
        self.login.page_login(phone, pwd)
