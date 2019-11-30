from page.loginpage import LoginPage
from log.user_log import UserLog
class LoginHandle(object):
    def __init__(self,driver):
        self.login_p = LoginPage(driver)
        get_user_log = UserLog()
        self.loger = get_user_log.get_log()

    def login_click(self):
        self.login_p.get_login_element().click()

    def send_username(self,username):
        self.loger.info('输入用户名')
        self.login_p.get_usenname_element().send_keys(username)

    def send_password(self,password):
        self.login_p.get_password_element().send_keys(password)

    def login_button_click(self):
        self.login_p.get_login_button_element().click()
