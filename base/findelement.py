from util.readini import ReadIin
class FindElement(object):
    def __init__(self,driver):
        self.driver = driver

    def get_element(self,key):
        read_ini = ReadIin()
        data = read_ini.get_vaule(key)
        by = data.split('>')[0]
        vaule = data.split('>')[1]
        if by == 'id':
            return self.driver.find_element_by_id(vaule)
        elif by == 'xpath':
            return self.driver.find_element_by_xpath(vaule)

