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
        text = "老板老板微信" + text
        speak(text=text)
        print(text)

    @itchat.msg_register(TEXT)
    def test(msg):
        print(TEXT)
        speak("老板老板我在线着呢")

    @itchat.msg_register(NOTE)
    def note(msg):
        print(msg)

    @itchat.msg_register(SYSTEM)
    def system(msg):
        print(msg)

    # @itchat.msg_register()
    # def s
if __name__ == '__main__':
    note()
    itchat.auto_login(hotReload=False)
    itchat.run()
# # 获取特定UserName的公众号，返回值为一个字典
# itchat.search_mps(userName='@abcdefg1234567')
# # 获取名字中含有特定字符的公众号，返回值为一个字典的列表
# itchat.search_mps(name='LittleCoder')
# # 以下方法相当于仅特定了UserName
# itchat.search_mps(userName='@abcdefg1234567', name='LittleCoder')