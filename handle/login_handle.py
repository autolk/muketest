from selenium.webdriver.common.keys import Keys
from page.loginpage import LoginPage
from page.loginpage import SearchPage
from log.user_log import UserLog
# 登录
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

# 搜索并加入购物车
class SearchHandle(object):
    def __init__(self,driver):
        self.login_p1 = SearchPage(driver)
        get_user_log = UserLog()
        self.loger = get_user_log.get_log()
    def first_page_click(self):
        self.login_p1.get_first_page_element().click()
    # 输入搜索内容并且回车
    def send_searh_text(self,text):
        self.login_p1.get_search_element().send_keys(text)
        self.login_p1.get_search_element().send_keys(Keys.ENTER)

    def list_click(self,driver):
        cur_handle = driver.current_window_handle
        self.login_p1.get_list_elememt().click()
        handles = driver.window_handles
        for handle in handles:
            if handle != cur_handle:
                driver.switch_to.window(handle)

    def shopping_click(self):
        self.login_p1.get_shopping_cart_element().click()