import unittest
import os
import time
from util.HTMLTestRunner import HTMLTestRunner
# import datetime
# class FirstTest(unittest.TestCase):
#     def test01(self):
#         print('11111111111111')
#     def test02(self):
#         print('22222222222')
#
# if __name__ == '__main__':
#
#     a = os.path.dirname(os.path.abspath(__file__))
#     b = os.path.dirname(a)
#     c = os.path.join(b, 'report')
#     report_file = datetime.datetime.now().strftime("%Y-%m-%d") + ".html"
#     report_name = c + '/' + report_file
#     print(report_name)
#     with open(report_name, "wb")as f:
#         suite = unittest.TestSuite()
#         # suite.addTest(FirstCase('test_login_code_error'))
#         suite.addTest(FirstTest('test01'))
#         # unittest.TextTestRunner().run(suite)
#         # suite = unittest.TestLoader().loadTestsFromTestCase(FirstCase)
#         runner = HTMLTestRunner(stream=f, title="This is first123 report", description=u"这个是我们第一次测试报告", verbosity=2)
#         runner.run(suite)





from selenium.webdriver.common.keys import Keys

from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.find_element_by_id('kw').send_keys('jjjj')

driver.find_element_by_id('kw').send_keys(Keys.ENTER)




















