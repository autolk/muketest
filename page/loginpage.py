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

#搜索并加入购物车
class SearchPage(object):
    def __init__(self,driver):
        self.fd1 = FindElement(driver)
    def get_first_page_element(self):
        return self.fd1.get_element('SearchElement','first_page')
    def get_search_element(self):
        return self.fd1.get_element('SearchElement','search_box')
    # def get_search_button_element(self):
    #     return self.fd1.get_element('SearchElement','search_button')
    def get_list_elememt(self):
        return self.fd1.get_element('SearchElement','list_title')
    def get_shopping_cart_element(self):
        return self.fd1.get_element('SearchElement','shopping_cart_button')