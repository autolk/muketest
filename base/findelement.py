from util.readini import ReadIin
class FindElement(object):
    def __init__(self,driver):
        self.driver = driver

    def get_element(self,file_name,node,key):
        read_ini = ReadIin(file_name)
        data = read_ini.get_vaule(node,key)
        by = data.split('>')[0]
        vaule = data.split('>')[1]
        try:
            if by == 'id':
                return self.driver.find_element_by_id(vaule)
            elif by == 'name':
                return self.driver.find_element_by_name(vaule)
            elif by == 'xpath':
                return self.driver.find_element_by_xpath(vaule)
            elif by == 'select':
                return self.driver.find_element_by_css_selector(vaule)
            elif by == 'alert':
                return self.driver.driver.switch_to.alert

        except:
            return None