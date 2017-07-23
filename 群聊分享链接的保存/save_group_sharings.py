#-*-coding：utf-8-*-
#！usr/bin/env python3


import itchat
from itchat.content import *
import re
import os, sqlite3
import datetime

def store(received_date=None, title=None,
          url=None, sharer=None,
          text=None):
    #数据库路径
    db_file = os.path.join(os.path.dirname(__file__), 'glinks.db')
    
    #当数据库文件glink.db存在直接插入
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        cursor.execute(r"insert into glinks values ('%s', '%s', '%s', '%s', '%s')" % (title, text, url, sharer, received_date))
    
    #当数据库文件glink.db不存在创建再插入
    except sqlite3.OperationalError:
        print('creating table glinks')
        cursor.execute('create table glinks(title text, text text,url text, sharer varchar(20), received_date text primary key )')
        cursor.execute(r"insert into glinks values ('%s', '%s', '%s', '%s', '%s')" % (title, text, url, sharer, received_date))
    
    try:  
        cursor.close()
        conn.commit()
        conn.close()
    except Exception as e:
        print(e)


def query_all():
    # 查询记录：
    
    conn = sqlite3.connect('glinks.db')
    cursor = conn.cursor()
    # 执行查询语句:
    # cursor.execute('select * from user where id=?', '1')
    cursor.execute('select * from glinks')
    # 获得查询结果集:
    values = cursor.fetchall()
    print(values)
    cursor.close()
    conn.close()



def find_text(content):
    content = content.replace(' ','A').replace('\n', 'A').replace('\t','A')
    pattern = r"<des>(.*?)</des>"
    r = re.compile(pattern)
    result = r.findall(content)[0]
    return result

def note():  
    @itchat.msg_register(['Sharing'],isGroupChat=True)
    def collect_links(msg):
        try:
            received_date = datetime.datetime.now()
            title = msg['FileName']
            url = msg['Url']
            sharer = msg['ActualNickName']
            text = find_text(content=msg['Content'])
            print(title, sharer, text, url, received_date)
            store(received_date=received_date,
                title=title,
                url=url,
                sharer=sharer,
                text=text)
            print('data stored done')
        except Exception as e:
            print(e)

if __name__ == '__main__':
    print('runing')
    note()
    itchat.auto_login(hotReload=True)
    itchat.run()
    # query_all()

