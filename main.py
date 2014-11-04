__author__ = 'imzihuang'
#coding:utf-8
from log import Log
from tornado.gen import coroutine
from tornado.curl_httpclient import CurlAsyncHTTPClient
from tornado.httpclient import HTTPRequest
import urllib
from tornado.ioloop import IOLoop
import sys
import thread
from mongo_control import SX_sms_log
import time


http_client = CurlAsyncHTTPClient()

@coroutine
def handle_msg(packet,count):
    #host="http://183.203.36.14:8777/sxm-crm-esop-pro/api/project/bbx/send_msg.json"
    host="http://localhost:8880/sxinterface/mq_sx"
    token_id = '3cbaec34-39d3-4eb2-bcac-0bc02e6a9667'

    uid = packet.get('n')
    p = packet.get('p')
    body = {'id': uid,
            'content': p,
            'token_id': token_id,
            }
    body=urllib.urlencode(body)
    print("Data:{0}".format(body))#当前参数


    try:
        log=Log()
        result_list=[]
        result=None
        for i in xrange(count):
            log.info_log("--------------------------begin------------------------------------------")
            log.info_log("data : {0}".format(body))
            result = yield http_client.fetch(HTTPRequest("{0}?{1}".format(host,body), method='GET'))
            result_sms=unicode("sms ok : {0}".format(result.body),"utf-8")
            log.info_log(result_sms)
            log.info_log("--------------------------end------------------------------------------")
            current=i+1
            requst_dic={
                "current request":current,
                "body request":result.body,
                "current_date":time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            }
            result_list.append(requst_dic)
            print("current request : {0}".format(current))
            print(result.body)
        #放在这里，后面可能存在异常
        sms_log=SX_sms_log()
        sms_log.recode_sms_sum(count,result_list)

    except Exception, ex:
        print('sms fail: {0}'.format(ex))
    print("end")
    sms_log.show_sms_sum_all()
    thread.exit()


def call(count):
    packet={"n":"lt_sx_1","p":"test"}
    handle_msg(packet,count)
    #handle= handle_msg(packet)
    """
    def mycall():
        IOLoop.current().add_callback(call)
    IOLoop.current().add_future(handle,mycall())
    """

if __name__=="__main__":
    sum=1#默认调用一次，可外部传值
    if len(sys.argv)>1:
        try:
            sum=int(sys.argv[1])
        except Exception,error:
            raise error
    print("begin")
    loop = IOLoop.instance()
    loop.add_callback(call,sum)
    loop.start()
