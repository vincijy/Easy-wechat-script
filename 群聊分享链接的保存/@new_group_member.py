#-*-coding：utf-8-*-
#！usr/bin/env python3

import itchat
from itchat.content import *
import re

def note():
    @itchat.msg_register(NOTE, isGroupChat=True)
    def deal_note(msg):
        try:
            pattern = r'邀请"(.*?)"加入了群聊'
            r = re.compile(pattern)
            result = r.findall(msg['Content'])[0]
            return(u"""
                    @%s
                    欢迎新同学，
                    """ % result)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    note()
    itchat.auto_login(hotReload=True)


