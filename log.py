__author__ = 'imzihuang'
#coding:utf-8

import logging
from logging.handlers import TimedRotatingFileHandler
import os
from os import path

class Log():
    log_path="./logs/css.log"
    def __init__(self):
        root = path.dirname(self.log_path)
        if not path.isdir(root):
            os.makedirs(root)
        log=logging.getLogger()
        log.setLevel(logging.NOTSET)
        hdlr = TimedRotatingFileHandler(self.log_path, when='D', backupCount=10, encoding='utf-8')
        hdlr.setFormatter(logging.Formatter('%(asctime)-15s [%(levelname)s] [%(process)d] [%(threadName)s] %(message)s'))
        log.addHandler(hdlr)
        self.log=log

    def debug_log(self,value):
        self.log.debug(value)

    def info_log(self,value):
        self.log.info(value)

    def error_log(self,value):
        self.log.error(value)




#gen_log = init_logger('./logs/css.log')
