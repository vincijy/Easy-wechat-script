#-*-coding：utf-8-*-
#！usr/bin/env python3

import itchat
import datetime

from apscheduler.schedulers.blocking import BlockingScheduler


task_list = [("02:35", "do A"),
             ("02:36", "do B"),
             ("21:27", "do C")]


def  task_remind():
    for task in task_list:
        task_time = task[0]
        task_content = task[1]
        if datetime.datetime.now().strftime("%H:%M") == task_time:
            #name=微信昵称
            receiver = itchat.search_friends(name=u"Hoder")[0]["UserName"]
            itchat.send_msg(task_content, receiver)

def remind_run():
    sched = BlockingScheduler()
    sched.add_job(task_remind, 'cron', second=0)
    sched.start()



if __name__ == '__main__':
    
    itchat.auto_login(hotReload=True)
    remind_run()
