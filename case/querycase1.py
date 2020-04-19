import unittest
import ddt
import time
import os
from bussiness.loginbussiness import LoginBusiness
from bussiness.querybussiness import QueryBusiness
from selenium import webdriver
from log.user_log import UserLog
from util.excel_util import ExcelUtil
# excel_login = ExcelUtil()
# login_data = excel_login.get_data()[1]


# 保单号
query_path = 'C:/Users/Administrator/Desktop/hexin/data/querydata.xls'
excel_query = ExcelUtil(query_path)
query_data = excel_query.get_data()[1]

# 投保单号
t_query_path = 'C:/Users/Administrator/Desktop/hexin/data/querydata.xls'
t_excel_query = ExcelUtil(t_query_path,1)
t_query_data = t_excel_query.get_data()[1]
# print(0000000000000000,t_query_data)

# 用户名
excel_path = 'C:/Users/Administrator/Desktop/hexin/data/logindata.xls'
excel_login = ExcelUtil(excel_path)
login_data = [excel_login.get_data()[1]]

@ddt.ddt
class LoginCsae(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.log = UserLog()
        cls.logger = cls.log.get_log()
        cls.driver = webdriver.Chrome()
        cls.driver.get('http://10.135.100.171:7001/life/main.jsp')
        cls.driver.maximize_window()

    def setUp(self):
        self.logger.info('this is chrom')
        self.login_b = LoginBusiness(self.driver)
        self.query_b = QueryBusiness(self.driver)


    # 登录
    @ddt.data(*login_data)
    def test_login(self,login_data):
        username,password = login_data
        b = self.login_b.user_base(username,password)
        self.assertEqual(b,'企业员工弹性福利')

    # 按照保单信息查询
    @ddt.data(*query_data)
    def test_query(self,query_data):
        policy_id = query_data
        c = self.query_b.query_base(policy_id)
        self.assertEqual(c,'jj')

    # 按照投保单信息查询
    # @ddt.data(*t_query_data)
    # def test_t_query(self,t_query_data):
    #     t_policy_id = t_query_data
    #     c = self.query_b.t_query_base(t_policy_id)
    #     self.assertEqual(c,'保单ID')

    def tearDown(self):
        time.sleep(2)
        for method_name, error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                filename = case_name + '.png'
                a = os.path.dirname(os.path.abspath(__file__))
                # b = os.path.dirname(a)
                c = os.path.join(a, 'Image')
                file_path = c + "/" + filename
                self.driver.save_screenshot(file_path)
                # print("这个是case的后置调键1")

    @classmethod
    def tearDownClass(cls):
        cls.log.close_handle()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()



