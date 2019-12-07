from page.searchpage import SearchPage
from log.user_log import UserLog
from selenium.webdriver.common.keys import Keys

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
        print('444444444444444')
        self.login_p1.get_list_elememt().click()
        handles = driver.window_handles
        print('3333333333')
        for handle in handles:
            if handle != cur_handle:
                driver.switch_to.window(handle)

    def shopping_click(self):
        print('11111')
        self.login_p1.get_shopping_cart_element().click()
        print('22222')