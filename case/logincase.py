import unittest
import ddt
import time
from bussiness.loginbussiness import LoginBusiness
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

    def tearDown(self):
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.log.close_handle()
        cls.driver.close()

    @ddt.data(*data)
    def test_login(self,data):
        username,password = data
        self.login_b.user_base(username,password)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(LoginCsae('test_login'))
    runner = unittest.TextTestRunner()
#     runner.run(suite)

