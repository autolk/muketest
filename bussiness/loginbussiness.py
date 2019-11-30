from handle.login_handle import LoginHandle
class LoginBusiness(object):
    def __init__(self,driver):
        self.login_h = LoginHandle(driver)

    def user_base(self,username,password):
        self.login_h.login_click()
        self.login_h.send_username(username)
        self.login_h.send_password(password)
        self.login_h.login_button_click()
