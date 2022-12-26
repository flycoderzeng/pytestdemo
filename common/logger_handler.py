# -*- coding: UTF-8 -*-
import logging
from logging.handlers import TimedRotatingFileHandler


class LoggerHandler(logging.Logger):
    def __init__(self, name: str, level: str = logging.DEBUG) -> None:
        super().__init__(name, level);
        self.setLevel(level);
        self.LOG_FORMAT = '[%(levelname)s] [%(asctime)s] [%(pathname)s] (%(funcName)s:%(lineno)d) %(message)s'
        self.add_stream_handler()
        self.add_file_handler()

    def add_stream_handler(self):
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(self.level)
        stream_handler.setFormatter(logging.Formatter(self.LOG_FORMAT))
        self.addHandler(stream_handler)

    def add_file_handler(self):
        '''
        filename: 日志文件名的prefix
        when: 是一个字符串，用于描述滚动周期的基本单位，字符串的值及意义如下：
         “S”: Seconds
         “M”: Minutes
         “H”: Hours
         “D”: Days
         “W”: Week day (0=Monday)
         “midnight”: Roll over at midnight
        interval: 滚动周期, 单位有when指定, 比如: when='D',interval=1, 表示每天产生一个日志文件;
        backupCount: 表示日志文件的保留个数；
        '''
        # 输出到文件 -----------------------------------------------------------
        # 按文件大小输出
        # 按时间输出
        file_handler = TimedRotatingFileHandler(filename='./logs/mypytest.log', when='D', interval=1, backupCount=365,
                                                encoding='utf-8')
        file_handler.setLevel(self.level)
        file_handler.setFormatter(logging.Formatter(self.LOG_FORMAT))
        self.addHandler(file_handler)

logger = LoggerHandler('root')