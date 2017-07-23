import time
import datetime
import itchat
import requests

from apscheduler.schedulers.blocking import BlockingScheduler


LOCATION = "上海"
REPORT_TIME = "07:40"

#接收信息的用户微信昵称列表
USER_NAME_LIST = [u"小明",u"小红"]

def get_weather(location):
    url = 'https://api.thinkpage.cn/v3/weather/daily.json'
    payload = {
        'days': 1,
        'key': 'lrtff1fcg9yym1bp',
        'location': location,
    }
    try:
        res = requests.get(url, params=payload)
        weather = res.json()['results'][0]['daily'][0]
        print(weather)
    except:
        return
    data = "%s 今日天气\n%s  \t%s℃~%s℃" % (location, weather['text_day'], weather['low'], weather['high'])
    if '雨' in weather['text_day']:
        data += '\n\n今天有雨，记得带伞啊。'
    data += '\n来自小机器人的温馨提示。'
    return data


def start(location=LOCATION, report_time=REPORT_TIME):

    if datetime.datetime.now().strftime('%H:%M') == report_time: #比如 03:25
        weather = ''
        count = 0
        while not weather:
            weather = get_weather(location)
            count += 1
            print('请求天气数据%d次' % count)
            time.sleep(1)
            if count >= 10:
                break
        if not weather:
            print('天气数据获取失败')
        else:
            #将信息发给用户
            for USER_NAME in USER_NAME_LIST:
                num = itchat.search_friends(name = USER_NAME)[0]["UserName"]
                try:
                    itchat.send_msg(get_weather(location), num)
                except Exception as e:
                    print(e)
                #print(get_weather(location))



if __name__ == '__main__':
    
    itchat.auto_login(hotReload=True)
    sched = BlockingScheduler()
    sched.add_job(start, 'cron', second=0)
    sched.start()