from handle.search_handle import SearchHandle

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