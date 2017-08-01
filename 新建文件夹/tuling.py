#coding=utf8
import requests
import itchat



def get_response_from_tuling_robot(message,tulingKey):

    defaultReply = 'I received: ' + message
    
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'    : tulingKey,
        'info'   : message,
        'userid' : 'wechat-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        
        return r.get('text')
    
    except:
        
        return defaultReply

#message=u'你叫什么名字'

#tulingKey='9eaf494cdd0a43429be85774b73d1e30'


