from handle.login_handle import LoginHandle
import time
class LoginBusiness(object):
    def __init__(self,driver):
        self.login_h = LoginHandle(driver)

    def user_base(self,username,password):
        self.login_h.send_username(username)
        self.login_h.send_password(password)
        self.login_h.login_button_click()
        time.sleep(5)
        a = self.login_h.get_sucess()
        return a

    # def login_sucess(self,username,password):
    #     self.user_base(username,password)
    #     time.sleep(5)
    #     a = self.login_h.get_sucess()
    #     return a

