# coding=utf-8
import logging
import os
import datetime


class UserLog(object):
    def __init__(self):
        self.logger1 = logging.getLogger(__name__)
        logging.Logger.manager.loggerDict.pop(__name__)
        self.logger1.handlers = []
        self.logger1.removeHandler(self.logger1.handlers)
        if not self.logger1.handlers:
            self.logger1.setLevel(logging.DEBUG)
            # 控制台输出日志
            # consle = logging.StreamHandler()
            # logger.addHandler(consle)

            # 文件名字
            base_dir = os.path.dirname(os.path.abspath(__file__))
            log_dir = os.path.join(base_dir, "logs")
            log_file = datetime.datetime.now().strftime("%Y-%m-%d") + ".log"
            log_name = log_dir + "/" + log_file
            # print(log_name)
            # 文件输出日志
            self.file_handle = logging.FileHandler(log_name, 'a', encoding='utf-8')
            self.file_handle.setLevel(logging.INFO)
            formatter = logging.Formatter('%(asctime)s %(filename)s--> %(funcName)s %(levelno)s: %(levelname)s ----->%(message)s')
            self.file_handle.setFormatter(formatter)
            self.logger1.addHandler(self.file_handle)

    def get_log(self):
        return self.logger1

    def close_handle(self):
        self.logger1.removeHandler(self.file_handle)
        self.file_handle.close()


if __name__ == '__main__':
    user = UserLog()
    log = user.get_log()
    log.debug('test')
    user.close_handle()

'''import logging
import os
import time
import datetime
class Logger(object):
    def __init__(self):
        """
        指定保存日志的文件路径，日志级别，调用文件
        将日志存入到指定的文件中
        :param logger:
        """
        # 创建一个logger(记录器)
        # 日志记录的工作主要由Logger对象来完成。在调用getLogger时要提供Logger的名称
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        # 创建一个handler，用于写入日志文件
        rq = datetime.datetime.now().strftime("%Y-%m-%d")
        base_dir = os.path.dirname(os.path.abspath(__file__))
        log_path = os.path.join(base_dir, "logs")
        log_name = log_path + rq + '.log' # 文件名

        # base_dir = os.path.dirname(os.path.abspath(__file__))
        # log_dir = os.path.join(base_dir, "logs")
        # log_file = datetime.datetime.now().strftime("%Y-%m-%d") + ".log"
        # log_name = log_dir + "/" + log_file
        # 将日志写入磁盘
        fh = logging.FileHandler(log_name)
        fh.setLevel(logging.INFO)
        # 创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getlog(self):
        return self.logger'''
