#coding=utf-8
 
#微信控制window系统PC示例
import os
import win32api
import itchat
from itchat.content import *


def open_txt():

    #打开与当前文件同目录下的test.txt文件
    path = os.path.abspath('.')

    file_path = os.path.join(path, 'test.txt')
    win32api.ShellExecute(0, 'open', file_path, '', '', 1)


def run():
    @itchat.msg_register(TEXT)
    def open(msg):
        if u'打开' in msg['Text']:
            open_txt()

if __name__ == '__main__':

    run()
    itchat.auto_login(hotReload=True)
    itchat.run()



