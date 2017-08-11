#coding=utf-8

import itchat
from itchat.content import *
import win32com.client


def speak(text):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(text)

def note():
    @itchat.msg_register(SHARING)
    def inform(msg):
        text=msg['Text']
        text = "微信" + text
        speak(text=text)
        print(text)




if __name__ == '__main__':
    note()
    itchat.auto_login(hotReload=False)
    itchat.run()
