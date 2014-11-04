__author__ = 'imzihuang'
#coding:utf-8
from mongo_control import SX_sms_log

def write_log():
    sms_log=SX_sms_log()
    sms_log.write_sms_info()

if __name__=="__main__":
    write_log()