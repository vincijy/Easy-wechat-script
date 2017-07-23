#coding=utf-8

import os

import itchat
from itchat.content import *

def reply():

    #群文件保存
    @itchat.msg_register(['Picture', 'Recording', 'Attachment', 'Video'],
                         isGroupChat=True
                         )

    def download_files(msg):

        chatroom_name = msg["User"]["NickName"]

        path = os.path.join(os.path.abspath("."),
                            "group_files"
                            )

        file_name_list = os.listdir(path)
        chatroom_file_location = os.path.join(os.path.abspath("."),
                                              "group_files","%s" % (chatroom_name)
                                              )

        if chatroom_name not in file_name_list:
            os.mkdir(chatroom_file_location)
        save_path = os.path.join(chatroom_file_location, msg['FileName'])
        msg['Text'](save_path)

    #群文件索要
    @itchat.msg_register(itchat.content.TEXT,
                         isGroupChat=True
                         )

    def text_reply(msg):
        
        if u'文件'in msg['Text']:

            chatroom_name = msg["User"]["NickName"]  # 群名称
            path = os.path.join(os.path.abspath("."), "group_files")  # 群文件
            file_name_list = os.listdir(path)
            chatroom_file_location = os.path.join(os.path.abspath("."),
                                                 "group_files",
                                                 "%s" % (chatroom_name)
                                                 )
            
            if chatroom_name not in file_name_list:
                os.mkdir(chatroom_file_location)
            

            filesName = u''
            fileList = [x for x in os.listdir(chatroom_file_location)]
            fileOder = 1  # 文件列表位置设定为1
            for file_name in fileList:
                filesName += "\n" + str(fileOder) + "  " + file_name
                fileOder += 1
            itchat.send(u'群文件在这里了，回复对应的数字获取' ,msg['FromUserName'])
            itchat.send(filesName, msg['FromUserName'])

            @itchat.msg_register('Text', isGroupChat=True)
            def send_file(msg):
                try:
                    print(msg['Text'])
                    fileIndent = (int(msg['Text'])-1)
                    file = fileList[fileIndent]
                    # file = file.decode('gbk')
                    # print('@fil@files/'+msg['Text'])
                    file_path = os.path.join(chatroom_file_location, file)
                    itchat.send_file(file_path, toUserName=msg['FromUserName'])
                    itchat.send(u'已经发送了，发送结束，如果还要文件，继续回复“文件”，回回复“帮助” 查看其它功能',
                                msg['FromUserName'])
                    reply()
                except:
                    itchat.send(u'发生了点错误啊啊啊,刚才叫你拿文件你干什么去了',
                                msg['FromUserName'])
                    reply()


if __name__ == '__main__':

    reply()
    itchat.auto_login(hotReload=True)
    itchat.run()



        

          
