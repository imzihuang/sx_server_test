#coding:utf-8
import pymongo
from pymongo import Connection
import time
import simplejson

class SX_sms_log():
    def __init__(self):
        db=Connection().sx_quest
        self.collection=db.sx_log
        """
        if self.collection.count()==0:
            dict={"title":"log_sx_sms","total":0}
            self.collection.insert(dict)
        """

    #记录当前请求次数
    def recode_sms_sum(self,sum,list):
        dict={
            "title":"log_sx_sms",
            "current_date":time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),
            "sum":sum,
            "request_list":list
        }
        self.collection.insert(dict)

    #显示请求记录
    def show_sms_sum_all(self):
        cursor= self.collection.find()
        for data in cursor:
            print(data)


    def clear_sms_sum(self):
        self.collection.remove({"title":"log_sx_sms"})

    def write_sms_info(self):
        output = open('./logs/{0}.txt'.format(time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))), 'w')
        cursor= self.collection.find()
        for data in cursor:
            del data["_id"]
            str_cursur=simplejson.dumps(r"{0}\t\n".format(data))
            output.writelines(str_cursur)



