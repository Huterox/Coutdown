# coding:utf-8
import datetime
from tkinter import *
import tkinter.messagebox
from weather import weather
import math,time
import os

def set_time(hour,minte,secends,day,month,year):
    way=r'D:\time _ show\time _ show\data'
    if not os.path.exists(way):
        os.makedirs(way)

    with open (r'D:\time _ show\time _ show\data\data_time.hly','w',encoding='utf-8') as f:
        set={}
        set['year']=str(year)
        set['month']=str(month)
        set['day']=str(day)
        set['hour']=str(hour)
        set['minter']=str(minte)
        set['secends']=secends
        f.write(str(set))
        f.close()


def show_time():
    try:
        x_path=r'D:\time _ show\time _ show\data\data_time.hly'
        if not os.path.exists(x_path):
                    set_time(00, 00, 00, 7, 7, 2020)

        global List
        global i
        root = Tk()
        List = []
        #root.title("a simple clock")
        #设置窗口是否可以变化长/宽
        screen_width=root.winfo_screenwidth()
        screen_heigh=root.winfo_screenheight()
        x=(screen_width-800)/2
        y=(screen_heigh-750)/2

        root.geometry('800x750+%d+%d'%(x,y))
        root.attributes('-alpha',0.5)
        root.attributes("-topmost", False)
        root.attributes("-toolwindow", True)
        root.overrideredirect(True)

        root.resizable(height=False,width=False)

        def points():
            for i in range(1, 13):
                x = 250 + 225 * math.sin(2 * math.pi * i / 12)

                y = 350 - 225 * math.cos(2 * math.pi * i / 12)

                canvas.create_text(x, y, text=i,font=('宋体','20'),fill='red')

        def createline(radius, line_width, rad):
            x = 250 + radius * math.sin(rad)

            y = 350 - radius * math.cos(rad)#指针末坐标

            i = canvas.create_line(250, 350, x, y, width=line_width,fill='red')#指针坐标

            List.append(i)

        canvas = Canvas(root, width=800, height=600, bd=0, highlightthickness=0)
        canvas.place(x=150,y=10)
        # 生成外圆
        #canvas.create_oval(50, 50, 350, 350)

        # 生成数字
        points()
        error=0
        try:
            weather_=weather()
            canvas.create_text(250, 30, text=weather_, font=('宋体', '25'), fill='red')

        except Exception as e :
            tkinter.messagebox.showwarning('警告By_Huterox','网路异常无法显示天气')
            error=e

        while 1:

            tm = time.localtime()
            if error!=0:
                try :

                    weather_ = weather()
                    canvas.create_text(250, 530, text=weather_, font=('宋体', '25'), fill='red')
                    error = 0
                except:
                    pass


            # cur_time=time.asctime(tm)
            cur_time2 = time.strftime('%Y-%m-%d %X', time.localtime())

            t_hour = 0

            if tm.tm_hour <= 12:

                t_hour = tm.tm_hour

            else:

                t_hour = tm.tm_hour - 12

            rad1 = 2 * math.pi * (t_hour + tm.tm_min / 60) / 12

            rad2 = 2 * math.pi * (tm.tm_min + tm.tm_sec / 60) / 60

            rad3 = 2 * math.pi * tm.tm_sec / 60

            createline(70, 8, rad1)

            createline(110, 4, rad2)

            createline(140, 2, rad3)
            year_ = datetime.datetime.today().year
            momth=6
            f=open(r'D:\time _ show\time _ show\data\data_time.hly','r',encoding='utf-8')
            f=f.read()
            safe={}
            f=eval(f,safe)
            momth=None
            if year_==2020:
                momth=7
            momth=int(f['month'])
            year_=int(f['year'])
            day=int(f['day'])
            last_time = datetime.datetime(year_, momth, day, 00, 00, 00)

            now_time=datetime.datetime.today()
            long_day=last_time - now_time
            long_day=long_day.days+1
            long_seconds=last_time - now_time
            #long_seconds=long_seconds.seconds
            text_j="离高考还有：%d天"%(long_day)
            if long_day <=1:
                text_j='鹏程万里，祝君提名'
            if long_day <=-2:
                text_j='倒计时重置'
                year_+=1


            time_text1 = canvas.create_text(250, 350, text=text_j, font=('宋体', '24'), fill='red')
            time_text = canvas.create_text(250, 450, text=cur_time2,font=('宋体','18'),fill='red')

            root.update()



            for item in List:
                canvas.delete(item)
            canvas.delete(time_text)
            canvas.delete(time_text1)

            # root.update()



        root.mainloop()
    except Exception as r:
        print(r)
if __name__=='__main__':
    show_time()