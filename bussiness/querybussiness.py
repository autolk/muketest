from handle.query_handle import QueryHandle
from handle.query_handle import TouQueryHandle
import time
class QueryBusiness(object):
    def __init__(self,driver):
        self.query_h = QueryHandle(driver)
        self.t_query_h = TouQueryHandle(driver)
    # 按照保单进行查询
    def query_base(self,policy_num):
        self.query_h.query_button_click()
        self.query_h.query2_button_click()
        self.query_h.query_style_click()
        time.sleep(2)
        self.query_h.send_policy_num(policy_num)
        self.query_h.find_button_click()
        time.sleep(5)
        a = self.query_h.get_sucess()
        return a

    # 按照投保单进行查询
    def t_query_base(self,t_policy_num):
        self.t_query_h.query_button_click()
        self.t_query_h.query2_button_click()
        self.t_query_h.query_style_click()
        time.sleep(2)
        self.t_query_h.send_t_policy_num(t_policy_num)
        self.t_query_h.find_button_click()
        time.sleep(5)
        a = self.t_query_h.get_sucess()
        return a