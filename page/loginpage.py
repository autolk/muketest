from base.findelement import FindElement

# 登录
class LoginPage(object):
    def __init__(self,driver):
        self.fd = FindElement(driver)
    def get_login_element(self):
        return self.fd.get_element('LoginElement','login_button')
    def get_usenname_element(self):
        return self.fd.get_element('LoginElement','user_name')
    def get_password_element(self):
        return self.fd.get_element('LoginElement','password')
    def get_login_button_element(self):
        return self.fd.get_element('LoginElement','login')
