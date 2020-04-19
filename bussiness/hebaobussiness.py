from handle.hebao_handle import HebaoHandle
import time
class HebaoBusiness(object):
    def __init__(self,driver):
        self.hebao_h = HebaoHandle(driver)

    # 按照保单进行查询
    def hebao_base(self,t_policy_num):
        self.hebao_h.hebao_button_click()
        self.hebao_h.hebao_button2_click()
        self.hebao_h.gedan_hebao_button_click()
        self.hebao_h.t_policy_num_send(t_policy_num)
        self.hebao_h.query_button_click()
        self.hebao_h.t_policy_num_button_click()
        self.hebao_h.alert_accept_button_click()
        self.hebao_h.select_all_button_click()
        self.hebao_h.to_dec_button_click()
