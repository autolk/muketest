import unittest
from util.HTMLTestRunner import HTMLTestRunner
import ddt
import time
import datetime
import os
from bussiness.loginbussiness import LoginBusiness
from bussiness.searchbusiness import SearchBussiness
from selenium import webdriver
from log.user_log import UserLog
from util.excel_util import ExcelUtil
excel_u = ExcelUtil()
data = excel_u.get_data()
@ddt.ddt
class LoginCsae(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.log = UserLog()
        cls.logger = cls.log.get_log()
        cls.driver = webdriver.Chrome()
        cls.driver.get('https://class.imooc.com/')
        cls.driver.maximize_window()

    def setUp(self):
        self.logger.info('this is chrom')
        self.login_b = LoginBusiness(self.driver)
        self.search_b = SearchBussiness(self.driver)

    @ddt.data(*data)
    def test_login(self,data):
        username,password = data
        self.login_b.user_base(username,password)

    def test_search(self):
        self.search_b.search_base('测试')

    def tearDown(self):
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.log.close_handle()
        cls.driver.quit()