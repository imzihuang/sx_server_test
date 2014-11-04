__author__ = 'imzihuang'
#coding:utf-8
from mongo_control import SX_sms_log

def clear_log():
    sms_log=SX_sms_log()
    sms_log.clear_sms_sum()

if __name__=="__main__":
    clear_log()