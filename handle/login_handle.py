from page.loginpage import LoginPage
from log.user_log import UserLog

# 登录
class LoginHandle(object):
    def __init__(self,driver):
        self.login_p = LoginPage(driver)
        get_user_log = UserLog()
        self.loger = get_user_log.get_log()

    def send_username(self,username):
        self.loger.info('这里是输入用户名')
        self.login_p.get_usenname_element().send_keys(username)


    def send_password(self,password):
        self.loger.info('这里是输入密码')
        self.login_p.get_password_element().send_keys(password)


    def login_button_click(self):
        self.loger.info('这里是点击登录')
        self.login_p.get_login_button_element().click()

    def get_sucess(self):
        return self.login_p.get_sucess_element().text


