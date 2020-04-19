from base.findelement import FindElement

# 登录
class LoginPage(object):
    def __init__(self,driver):
        self.file_name = 'C:/Users/Administrator/Desktop/hexin/config/LoginElement.ini'
        self.fd = FindElement(driver)
    def get_usenname_element(self):
        return self.fd.get_element(self.file_name,'LoginElement','user_name')
    def get_password_element(self):
        return self.fd.get_element(self.file_name,'LoginElement','password')
    def get_login_button_element(self):
        return self.fd.get_element(self.file_name,'LoginElement','login')
    def get_sucess_element(self):
        return self.fd.get_element(self.file_name,'LoginElement','assert')

