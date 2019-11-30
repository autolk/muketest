from base.findelement import FindElement

class LoginPage(object):
    def __init__(self,driver):
        self.fd = FindElement(driver)
    def get_login_element(self):
        return self.fd.get_element('login_button')
    def get_usenname_element(self):
        return self.fd.get_element('user_name')
    def get_password_element(self):
        return self.fd.get_element('password')
    def get_login_button_element(self):
        return self.fd.get_element('login')