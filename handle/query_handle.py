from log.user_log import UserLog
from base.findelement import FindElement


# 按照保单进行查询
class QueryHandle(object):
    def __init__(self,driver):
        self.file_name = 'C:/Users/Administrator/Desktop/hexin/config/QueryElement.ini'
        self.fd = FindElement(driver)
        get_user_log = UserLog()
        self.loger = get_user_log.get_log()

    def query_button_click(self):
        self.loger.info('这里是点击综合查询')
        # self.query_p.get_query_button_element().click()
        self.fd.get_element(self.file_name,'PolicyQueryElement', 'query_button').click()

    def query2_button_click(self):
        self.loger.info('这里是点击综合查询2')
        # self.query_p.get_query2_button_element().click()
        self.fd.get_element(self.file_name,'PolicyQueryElement', 'query2_button').click()

    def query_style_click(self):
        self.loger.info('选择按保单信息查询')
        # self.query_p.get_query_style_element().click()
        self.fd.get_element(self.file_name,'PolicyQueryElement', 'query_style').click()

    def send_policy_num(self,policy_num):
        self.loger.info('输入保单号')
        # self.query_p.get_policy_num_element().send_keys(policy_num)
        self.fd.get_element(self.file_name,'PolicyQueryElement', 'policy_num').send_keys(policy_num)

    def find_button_click(self):
        self.loger.info('点击查询')
        self.fd.get_element(self.file_name,'PolicyQueryElement', 'find_button').click()

    def get_sucess(self):
        return self.fd.get_element(self.file_name,'PolicyQueryElement','assert').text

# 按照投保单进行查询
class TouQueryHandle(object):
    def __init__(self,driver):
        self.file_name = 'C:/Users/Administrator/Desktop/hexin/config/QueryElement.ini'
        self.fd = FindElement(driver)
        get_user_log = UserLog()
        self.loger = get_user_log.get_log()

    def query_button_click(self):
        self.loger.info('这里是点击综合查询')
        self.fd.get_element(self.file_name,'t_PolicyQueryElement','query_button').click()

    def query2_button_click(self):
        self.loger.info('这里是点击综合查询2')
        self.fd.get_element(self.file_name,'t_PolicyQueryElement','query2_button').click()

    def query_style_click(self):
        self.loger.info('选择按投保单信息查询')
        self.fd.get_element(self.file_name,'t_PolicyQueryElement','query_style').click()

    def send_t_policy_num(self,t_policy_num):
        self.loger.info('输入投保单号')
        self.fd.get_element(self.file_name,'t_PolicyQueryElement','t_policy_num').send_keys(t_policy_num)

    def find_button_click(self):
        self.loger.info('选择按投保单信息查询')
        self.fd.get_element(self.file_name,'t_PolicyQueryElement','find_button').click()

    def get_sucess(self):
        self.loger.info('返回保单ID')
        return self.fd.get_element(self.file_name,'t_PolicyQueryElement','assert').text

