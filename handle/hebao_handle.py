from log.user_log import UserLog
from base.findelement import FindElement

# 按照保单进行查询
class HebaoHandle(object):
    def __init__(self,driver):
        self.file_name = 'C:/Users/Administrator/Desktop/hexin/config/HebaoElement.ini'
        self.fd = FindElement(driver)
        get_user_log = UserLog()
        self.loger = get_user_log.get_log()

    def hebao_button_click(self):
        self.loger.info('这里是点击核保')
        self.fd.get_element(self.file_name,'IndexElement', 'hebao_button').click()

    def hebao_button2_click(self):
        self.loger.info('这里是点击核保2')
        self.fd.get_element(self.file_name,'IndexElement', 'hebao_button2').click()

    def gedan_hebao_button_click(self):
        self.loger.info('这里是点击核保')
        self.fd.get_element(self.file_name,'IndexElement', 'gedan_hebao_button').click()

    def t_policy_num_send(self,t_policy_num):
        self.loger.info('这里是输入投保单号')
        self.fd.get_element(self.file_name,'QueryElement', 't_policy_num').send_keys(t_policy_num)

    def query_button_click(self):
        self.loger.info('这里是点击查询')
        self.fd.get_element(self.file_name,'QueryElement', 'query_button').click()

    def t_policy_num_button_click(self):
        self.loger.info('这里是点击投保单号按钮')
        self.fd.get_element(self.file_name,'QueryElement', 't_policy_num_button').click()

     # 注意这块有个弹窗
    def alert_accept_button_click(self):
        self.loger.info('这里是点击弹窗确定按钮')
        self.fd.get_element(self.file_name, 'HebaoElement', 'alert_accept').accept()

    def select_all_button_click(self):
        self.loger.info('这里是点击全选按钮')
        self.fd.get_element(self.file_name,'HebaoElement', 'select_all_button').click()

    def to_dec_button_click(self):
        self.loger.info('这里是点击给出险种核保决定按钮')
        self.fd.get_element(self.file_name,'HebaoElement', 'to_dec_button').click()