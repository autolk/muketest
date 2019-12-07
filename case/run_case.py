import unittest
import os
import datetime
from util.HTMLTestRunner import HTMLTestRunner
# test_dir = './'
# disconver = unittest.defaultTestLoader.discover(test_dir, pattern='*case.py')
# runner=unittest.TextTestRunner()
# runner.run(disconver)



if __name__ == '__main__':

    test_dir = './'
    disconver = unittest.defaultTestLoader.discover(test_dir, pattern='*case.py')
    a = os.path.dirname(os.path.abspath(__file__))
    b = os.path.dirname(a)
    c = os.path.join(b, 'report')
    report_file = datetime.datetime.now().strftime("%Y-%m-%d") + ".html"
    report_name = c + '/' + report_file
    print(report_name)
    with open(report_name, "wb")as f:
        runner = HTMLTestRunner(stream=f, title="This is first report1", description=u"这个是我们第一次测试报告1", verbosity=2)
        runner.run(disconver)

