from handle.login_handle import LoginHandle
from handle.login_handle import SearchHandle
class LoginBusiness(object):
    def __init__(self,driver):
        self.login_h = LoginHandle(driver)

    def user_base(self,username,password):
        self.login_h.login_click()
        self.login_h.send_username(username)
        self.login_h.send_password(password)
        self.login_h.login_button_click()

class SearchBussiness(object):
    def __init__(self,driver):
        self.driver = driver
        self.search_h = SearchHandle(driver)
    def search_base(self,text):
        self.search_h.first_page_click()
        self.search_h.send_searh_text(text)
        # self.search_h.search_click()
        self.search_h.list_click(self.driver)
        self.search_h.shopping_click()