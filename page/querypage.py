from base.findelement import FindElement

# 按照保单进行查询
class QueryPage(object):
    def __init__(self,driver):
        self.fd = FindElement(driver)

    def get_query_button_element(self):
        return self.fd.get_element('PolicyQueryElement','query_button')

    def get_query2_button_element(self):
        return self.fd.get_element('PolicyQueryElement','query2_button')

    def get_query_style_element(self):
        return self.fd.get_element('PolicyQueryElement','query_style')

    def get_policy_num_element(self):
        return self.fd.get_element('PolicyQueryElement','policy_num')


    def get_find_button_element(self):
        return self.fd.get_element('PolicyQueryElement','find_button')

    def get_sucess_element(self):
        return self.fd.get_element('PolicyQueryElement','assert')