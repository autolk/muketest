import unittest
from util.HTMLTestRunner import HTMLTestRunner
import ddt
import time
import datetime
import os
from bussiness.loginbussiness import LoginBusiness
from selenium import webdriver
from log.user_log import UserLog
# from log.user_log import Logger
from util.excel_util import ExcelUtil

excel_path = 'C:/Users/Administrator/Desktop/hexin/data/logindata.xls'
excel_login = ExcelUtil(excel_path)
login_data = excel_login.get_data()[1]

@ddt.ddt
class LoginCsae(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.log = UserLog()
        cls.logger = cls.log.get_log()
        # cls.driver = webdriver.Chrome()
        # cls.driver.get('http://10.135.100.171:7001/life/main.jsp')
        # cls.driver.maximize_window()

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://10.135.100.171:7001/life/main.jsp')
        self.driver.maximize_window()

        self.logger.info('this is chrom')
        self.login_b = LoginBusiness(self.driver)


    @ddt.data(*login_data)
    def test_login(self,login_data):
        username,password = login_data
        b = self.login_b.user_base(username,password)
        self.assertEqual(b,'111')
        # self.assertEqual(b,'企业员工弹性福利')

    def tearDown(self):
        time.sleep(2)
        for method_name, error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                filename = case_name + '.png'
                a = os.path.dirname(os.path.abspath(__file__))
                b = os.path.dirname(os.path.dirname(a))
                c = os.path.join(b, 'Image')
                file_path = c + "/" + filename
                self.driver.save_screenshot(file_path)
                # print("这个是case的后置调键1")
        self.driver.quit()

    @classmethod
    def tearDownClass(cls):
        cls.log.close_handle()
        # cls.driver.quit()


if __name__ == '__main__':
    unittest.main()

    # suite = unittest.TestSuite()
    # suite.addTest(LoginCsae('test_login'))
    # suite.addTest(LoginCsae('test_search'))
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
    # a = os.path.dirname(os.path.abspath(__file__))
    # b = os.path.dirname(a)
    # c = os.path.join(b, 'report')
    # report_file = datetime.datetime.now().strftime("%Y-%m-%d") + ".html"
    # report_name = c + '/' + report_file
    # print(report_name)
    # with open(report_name, "wb")as f:
    #     suite = unittest.TestLoader().loadTestsFromTestCase(LoginCsae)
    #     runner = HTMLTestRunner(stream=f, title="This is first report1", description=u"这个是我们第一次测试报告1", verbosity=2)
    #     runner.run(suite)
        # suite11 = unittest.TestSuite()
        # # suite.addTest(FirstCase('test_login_code_error'))
        # suite.addTest(LoginCsae('test_login'))
        # # unittest.TextTestRunner().run(suite)
        # # suite = unittest.TestLoader().loadTestsFromTestCase(FirstCase)
        # runner = HTMLTestRunner(stream=f, title="This is first123 report", description=u"这个是我们第一次测试报告", verbosity=2)
        # runner.run(suite)




