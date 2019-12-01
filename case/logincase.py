import unittest
from util.HTMLTestRunner import HTMLTestRunner
import ddt
import time
import datetime
import os
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

    @ddt.data(*data)
    def test_login(self,data):
        username,password = data
        self.login_b.user_base(username,password)

    def tearDown(self):
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.log.close_handle()
        cls.driver.close()



if __name__ == '__main__':

    suite = unittest.TestSuite()
    suite.addTest(LoginCsae('test_login'))
    runner = unittest.TextTestRunner()
    runner.run(suite)
    a = os.path.dirname(os.path.abspath(__file__))
    b = os.path.dirname(a)
    c = os.path.join(b, 'report')
    report_file = datetime.datetime.now().strftime("%Y-%m-%d") + ".html"
    report_name = c + '/' + report_file
    print(report_name)
    with open(report_name, "wb")as f:
        suite = unittest.TestLoader().loadTestsFromTestCase(LoginCsae)
        runner = HTMLTestRunner(stream=f, title="This is first report1", description=u"这个是我们第一次测试报告1", verbosity=2)
        runner.run(suite)
        # suite = unittest.TestSuite()
        # # suite.addTest(FirstCase('test_login_code_error'))
        # suite.addTest(LoginCsae('test_login'))
        # # unittest.TextTestRunner().run(suite)
        # # suite = unittest.TestLoader().loadTestsFromTestCase(FirstCase)
        # runner = HTMLTestRunner(stream=f, title="This is first123 report", description=u"这个是我们第一次测试报告", verbosity=2)
        # runner.run(suite)


