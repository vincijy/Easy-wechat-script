#coding=utf-8

import itchat
from itchat.content import SHARING, TEXT
import win32com.client


def speak(text):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(text)

def note():   
    @itchat.msg_register(SHARING)
    def inform(msg):
        text=msg['Text']
        text = "老板老板" + text
        speak(text=text)

    @itchat.msg_register(TEXT)
    def test(msg):
        speak("老板老板我在线着呢")
if __name__ == '__main__':
    note()
    itchat.auto_login(hotReload=True)
    itchat.run()