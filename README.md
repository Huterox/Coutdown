
高中写的一个高考倒计时的倒计时程序，给有需要的人😉
（由于GitHub的markdown不太支持某些特殊的标记（CSDN与这里的编辑器有所区别）所以说明文档的观看体验可能不如直接在CSDN查看原版博客。（csdn博客地址为：https://blog.csdn.net/FUTEROX/article/details/107869258）

![image](https://user-images.githubusercontent.com/62883004/124929503-25f99680-e033-11eb-99da-f04fbaa1ad4f.png)


## 计时器部分
Canve.py
这个呢是用python开发的，而且只是使用tkinter开发的，所以相信还是有一定的参考能力的。
**奉上代码**

```python
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
        x=(screen_width-600)/2
        y=(screen_heigh-550)/2

        root.geometry('600x550+%d+%d'%(x,y))
        root.attributes('-alpha',0.5)
        root.attributes("-topmost", False)
        root.attributes("-toolwindow", True)
        root.overrideredirect(True)

        root.resizable(height=False,width=False)

        def points():
            for i in range(1, 13):
                x = 200 + 180 * math.sin(2 * math.pi * i / 12)

                y = 250 - 180 * math.cos(2 * math.pi * i / 12)

                canvas.create_text(x, y, text=i,font=('宋体','20'),fill='red')

        def createline(radius, line_width, rad):
            x = 200 + radius * math.sin(rad)

            y = 250 - radius * math.cos(rad)#指针末坐标

            i = canvas.create_line(200, 250, x, y, width=line_width,fill='red')#指针坐标

            List.append(i)

        canvas = Canvas(root, width=400, height=600, bd=0, highlightthickness=0)
        canvas.pack()
        # 生成外圆
        #canvas.create_oval(50, 50, 350, 350)

        # 生成数字
        points()
        error=0
        try:
            weather_=weather()
            canvas.create_text(200, 30, text=weather_, font=('宋体', '15'), fill='red')

        except Exception as e :
            tkinter.messagebox.showwarning('警告By_Huterox','网路异常无法显示天气')
            error=e

        while 1:

            tm = time.localtime()
            if error!=0:
                try :

                    weather_ = weather()
                    canvas.create_text(200, 30, text=weather_, font=('宋体', '15'), fill='red')
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

            createline(50, 6, rad1)

            createline(90, 3, rad2)

            createline(120, 1, rad3)
            year_ = datetime.datetime.today().year
            momth=6
            f=open(r'D:\time _ show\time _ show\data\data_time.hly','r',encoding='utf-8')
            f=f.read()
            safe={}
            f=eval(f,safe)

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
            if long_day <=3:
                text_j='鹏程万里，祝君提名'
            if long_day <=-2:
                text_j='倒计时重置'
                year_+=1


            time_text1 = canvas.create_text(200, 300, text=text_j, font=('宋体', '18'), fill='red')
            time_text = canvas.create_text(200, 500, text=cur_time2,font=('宋体','18'),fill='red')

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
```

**这里是计时器部分，当然这里只是其中一个部分隶属于项目子文件。**
## 项目结构
为了更好的了解，我们来了解一下项目结构：



![在这里插入图片描述](https://img-blog.csdnimg.cn/20200624170651665.png)
**这里的Canvas就是计时器，至于datetime我只是把模块移到了项目里面。不要在意。**
## 控制器
control.py
代码如下：

```python
from PIL import Image,ImageTk
import tkinter.messagebox
import os
from set_black import setWallPaper
from ground import save_url,load_view,load_down,root_url
import tkinter
import datetime
y=datetime.datetime.today().year
m=datetime.datetime.today().month




def set_time(hour,minte,secends,day,month=str(m),year=str(y)):
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

    f=open (r'D:\time _ show\time _ show\data\data_time.hly','r',encoding='utf-8')
    safe={}
    dic=f.read()
    dic=eval(dic,safe)
    #print(dic['year'])

#set_time(00,00,00,7,month=7)
class Win:
    def __init__(self):
        self.safe = {}
        self.page_index='index_{}.html'
        self.way = r'D:\time _ show\time _ show\data'

        if not os.path.exists(self.way):
            os.makedirs(self.way)
        self.use_path=r'D:\time _ show\time _ show\data\use_date.hly'
        if not os.path.exists(self.use_path):
            f=open(self.use_path,'w')
            f.close()

        with open(r'D:\time _ show\time _ show\data\use_date.hly','r') as f:
                self.use_date = {}
                if   f.read()=='':
                    f.close()
                    with open(r'D:\time _ show\time _ show\data\use_date.hly', 'w') as f:
                        self.use_date['page'] = 2

                        self.use_date['view_picture']=0
                        self.use_date['url']='http://pic.netbian.com/index_{}.html'
                        f.write(str(self.use_date))
                        f.close()

        with open(r'D:\time _ show\time _ show\data\use_date.hly', 'r') as f:
                self.r_=f.read()
                self.r_=eval(self.r_,self.safe)
            #print(type(self.r_))
                self.page = self.r_['page']
                self.view_picture = self.r_['view_picture']
                self.url=self.r_['url']
                f.close()
        with open(r'D:\time _ show\time _ show\data\view_url.hly', 'w+') as f:
                if   f.read()=='':
                    f.close()
                    ux = 'http://pic.netbian.com/index.html'
                    root_url(ux)



        self.win=tkinter.Tk()
        self.win.geometry('600x600')
        self.win.title('Control_v0.1')
        self.win.attributes('-toolwindow',True)

    def Label(self):
        self.Label_year=tkinter.Label(self.win,text='输入高考年份:',font=('宋体',11),justify="left")
        self.Label_year.place(x=25,y=25,width=100,height=25)
        self.Label_month = tkinter.Label(self.win, text='输入高考月份:', font=('宋体', 11),justify="left")
        self.Label_month.place(x=25, y=75, width=100, height=25)
        self.Label_day = tkinter.Label(self.win, text='输入高考天数:', font=('宋体', 11),justify="left")
        self.Label_day.place(x=25, y=125, width=100, height=25)
        self.Label_day = tkinter.Label(self.win, text='壁纸预览：', font=('宋体', 11), justify="left")
        self.Label_day.place(x=0, y=205, width=100, height=25)

    def Entry(self):
        self.entry_year=tkinter.Entry(self.win,font=('宋体', 14))
        self.entry_year.place(x=150,y=25,width=150,height=25)

        self.entry_month=tkinter.Entry(self.win,font=('宋体', 14))
        self.entry_month.place(x=150,y=75,width=150,height=25)

        self.entry_day=tkinter.Entry(self.win,font=('宋体', 14))
        self.entry_day.place(x=150,y=125,width=150,height=25)
        self.day = self.entry_day.get()
    def command_year(self):
        self.year=str(self.entry_year.get())
        set_time(00, 00, 00, 7,7, self.year)
    def command_month(self):
        self.month=str(self.entry_month.get())
        set_time(00,00,00,7,self.month,self.year)
    def command_day(self):
        self.day=str(self.entry_day.get())
        set_time(00,00,00,self.day,self.month,self.year)
    def commad_default(self):
        set_time(00,00,00,7,7,2020)
    def link_author(self):
        tkinter.messagebox.showinfo('tips','Q3139541502\n68元获取完整代码\n附赠全套python或C++学习资源')


    def Button(self):
        self.year = self.entry_year.get()
        self.month = self.entry_month.get()
        self.day = self.entry_day.get()
        self.Button_year=tkinter.Button(self.win,font=('宋体', 14),text='确定',relief='groove',command=lambda :Win.command_year(self))
        self.Button_year.place(x=325,y=25,width=100,height=25)
        self.Button_month=tkinter.Button(self.win,font=('宋体', 14),text='确定',relief='groove',command=lambda :Win.command_month(self))
        self.Button_month.place(x=325,y=75,width=100,height=25)
        self.Button_day=tkinter.Button(self.win,font=('宋体', 14),text='确定',relief='groove',command=lambda :Win.command_day(self))
        self.Button_day.place(x=325,y=125,width=100,height=25)
        self.Button_default=tkinter.Button(self.win,font=('宋体', 14),text='默认',relief='groove',command=lambda :Win.commad_default(self))
        self.Button_default.place(x=25, y=175, width=150, height=25)
        self.Button_link = tkinter.Button(self.win, font=('宋体', 14), text='联系作者', relief='groove',command=lambda :Win.link_author(self))

        self.Button_link.place(x=240, y=175, width=200, height=25)
    def view_next(self):
            #print(self.page)
            #print(self.view_picture)
            with open(r'D:\time _ show\time _ show\data\view_url.hly','r') as f:
                m=f.read()
                f.close()
                m=eval(m,self.safe)
                try:
                    use_url=m[self.view_picture]

                    try:
                        load_view(use_url)
                    except  Exception as e:
                        self.view.configure(text=str(e), font=('宋体', 14))

                    with open(r'D:\time _ show\time _ show\data\use_date.hly', 'w') as f:
                        self.view_picture+=1

                        self.r_={}
                        # print(type(self.r_))
                        self.r_['page']=self.page
                        self.r_['view_picture']=self.view_picture
                        self.r_['url']=self.url
                        f.write(str(self.r_))
                        f.close()
                except Exception as error:

                    with open(r'D:\time _ show\time _ show\data\use_date.hly', 'r') as f:
                        m = f.read()
                        f.close()
                        m = eval(m, self.safe)
                        page=m['page']
                        url=self.url.format(str(page))
                        #print(url)
                    save_url(url)
                    #print(self.url)
                    #print(type(self.url))
                    self.page+=1

                    with open(r'D:\time _ show\time _ show\data\use_date.hly', 'w') as f:
                        self.r_={}
                        self.r_['page']=self.page
                        self.r_['view_picture']=self.view_picture
                        self.r_['url']=self.url
                        f.write(str(self.r_))
                        f.close()


            self.img = Image.open(r'D:\time _ show\picture\view\view.jpg')
            self.img1 = ImageTk.PhotoImage(self.img)
            self.view.configure(image=self.img1, compound="center",text='')


    def view_last(self):
            self.view_picture -= 2

            if self.view_picture<0:
                self.view_picture = 0
                self.view.configure(text='已经是第一张', font=('宋体', 14))
            #print(self.page)
            #print(self.view_picture)
            elif self.view_picture>=0:
                with open(r'D:\time _ show\time _ show\data\view_url.hly','r') as f:
                    m=f.read()
                    f.close()
                    m=eval(m,self.safe)
                    use_url=m[self.view_picture]
                    with open(r'D:\time _ show\time _ show\data\use_date.hly', 'w') as f:

                        self.r_={}
                            # print(type(self.r_))
                        self.r_['page']=self.page
                        self.r_['view_picture']=self.view_picture
                        self.r_['url']=self.url
                        f.write(str(self.r_))
                        f.close()


            try:
                load_view(use_url)
            except  Exception as e:
                self.view.configure(text=str(e),font=('宋体',14))

            self.img = Image.open(r'D:\time _ show\picture\view\view.jpg')
            self.img1 = ImageTk.PhotoImage(self.img)
            self.view.configure(image=self.img1, compound="center",text='')
            self.view_picture+=1


    def set_ground(self):
        with open(r'D:\time _ show\time _ show\data\download_url.hly', 'r') as f:
            m = f.read()
            f.close()
            m = eval(m, self.safe)
            l=self.view_picture
            l-=1
            if l<=0:
                l=0
            use_url = m[l]

        try:
            path=load_down(use_url,name=self.view_picture)

            #print(path)
            path_=r'D:\time _ show\picture\download\{}.jpg'
            path_ = path_.format(str(self.view_picture))
            setWallPaper(path_)
        except  Exception as e:
            self.view.configure(text=str(e), font=('宋体', 14))


    def view(self):

        self.view=tkinter.Label(self.win,text='点击下一页加载图片',font=('宋体',14))
        self.view.place(x=75,y=230,width=460, height=300)

        self.last=tkinter.Button(self.win,font=('宋体', 14),text='<',relief='groove',command=lambda :Win.view_last(self))
        self.last.place(x=40,y=230,width=20, height=300)
        self.next=tkinter.Button(self.win,font=('宋体', 14),text='>',relief='groove',command=lambda :Win.view_next(self))
        self.next.place(x=540,y=230,width=20, height=300)
        self.set_ground=tkinter.Button(self.win,font=('宋体', 14),text='设置为壁纸',relief='groove',command=lambda :Win.set_ground(self))
        self.set_ground.place(x=470,y=535,width=100, height=40)

    def mainloop(self):
        self.win.mainloop()



if __name__=='__main__':

    win=Win()
    win.Label()
    win.Entry()
    win.Button()
    win.view()
    win.mainloop()



```

## 壁纸获取
ground.py

```python
import urllib.request
import os
import re

def root_url(url):
    try:
        url=url
        headers={'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Mobile Safari/537.36 SE 2.X MetaSr 1.0'}
        respon=urllib.request.Request(url=url,headers=headers)

        reason=urllib.request.urlopen(respon)
        reason=reason.read().decode('gbk')
        path_main='</b></a></li><li><a href="(.*?)" title='
        path_view='target="_blank"><span><img src="(.*?)" alt='
        path_download='<a href="" id="img"><img src="(.*)" data-pic="'
        path_download=re.compile(path_download,re.M)

        path_main=re.compile(path_main,re.M)
        path_view=re.compile(path_view,re.M)

        path_main=path_main.findall(reason)
        path_view=path_view.findall(reason)
        main_url = []
        #print(path_main)


        u_='http://pic.netbian.com'
        view_url=[]
        download_url=[]

        for i in path_main:
            u=u_+i
            main_url.append(u)
        for i in path_view:
            v=u_+i
            view_url.append(v)
        view_url.remove(view_url[0])
        for i in main_url:
            req=urllib.request.Request(url=str(i),headers=headers)
            reason_=urllib.request.urlopen(req)
            reason_=reason_.read().decode('gbk')
            u_l=path_download.findall(reason_)[0]
            ul=u_+u_l

            download_url.append(ul)
        way=r'D:\time _ show\time _ show\data'
        if not os.path.exists(way):
            os.makedirs(way)
        with open(r'D:\time _ show\time _ show\data\view_url.hly','w',encoding='utf-8') as f :
            f.write(str(view_url))
            f.close()
        with open(r'D:\time _ show\time _ show\data\download_url.hly','w',encoding='utf-8') as f :
            f.write(str(download_url))
            f.close()
            #print(download_url)

    except Exception as e:
        pass
    
    
def save_url(url):
    way = r'D:\time _ show\time _ show\data\exit'
    if not os.path.exists(way):

        urx = 'http://pic.netbian.com/index.html'
        root_url(urx)
        os.makedirs(way)

    headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Mobile Safari/537.36 SE 2.X MetaSr 1.0'}
    respon = urllib.request.Request(url=url, headers=headers)
    reason = urllib.request.urlopen(respon)
    reason = reason.read().decode('gbk')
    path_main = '</b></a></li><li><a href="(.*?)" target="_blank">'
    path_view = ' target="_blank"><img src="(.*?)" alt='
    path_download = '<a href="" id="img"><img src="(.*)" data-pic="'
    path_download = re.compile(path_download, re.S)
    path_main = re.compile(path_main, re.M)
    path_view = re.compile(path_view, re.M)
    path_main = path_main.findall(reason)
    path_view = path_view.findall(reason)
    main_url = []
    #print(path_main)
    #print(path_view)

    m_v=open(r'D:\time _ show\time _ show\data\view_url.hly','r',encoding='utf-8')
    mv=m_v.read()
    m_v.close()
    mv_={}
    view_url=eval(mv,mv_)
    m_l = open(r'D:\time _ show\time _ show\data\download_url.hly', 'r', encoding='utf-8')
    ml=m_l.read()
    m_l.close()
    ml_={}
    download_url=eval(ml,ml_)

    u_ = 'http://pic.netbian.com'
    for i in path_main:
        u = u_ + i

        main_url.append(u)
    for i in path_view:
        v = u_ + i
        view_url.append(v)
    view_url.remove(view_url[0])
    for i in main_url:
        req = urllib.request.Request(url=str(i), headers=headers)
        reason_ = urllib.request.urlopen(req)
        reason_ = reason_.read().decode('gbk')
        u_l = path_download.findall(reason_)[0]
        ul = u_ + u_l
        download_url.append(ul)
    with open(r'D:\time _ show\time _ show\data\view_url.hly', 'w', encoding='utf-8') as f:
        f.write(str(view_url))
        f.close()
    with open(r'D:\time _ show\time _ show\data\download_url.hly', 'w', encoding='utf-8') as f:
        f.write(str(download_url))
        f.close()
        print(len(download_url))



def load_view(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Mobile Safari/537.36 SE 2.X MetaSr 1.0'}
    reqs=urllib.request.Request(url=url,headers=headers)
    pic=urllib.request.urlopen(reqs)
    pic=pic.read()
    way=r'D:\time _ show\picture\view'
    if not os.path.exists(way):
        os.makedirs(way)
    with open(r'D:\time _ show\picture\view\view.jpg','wb') as view:
        view.write(pic)
        view.close()

def load_down(url,name):
    headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Mobile Safari/537.36 SE 2.X MetaSr 1.0'}
    reqs=urllib.request.Request(url=url,headers=headers)
    pic=urllib.request.urlopen(reqs)
    pic=pic.read()
    way=r'picture\download'
    load_path_=r'D:\time _ show\picture\download\{}.jpg'
    load_path=load_path_.format(str(name))
    if not os.path.exists(way):
        os.makedirs(way)
    with open(load_path,'wb') as view:
        view.write(pic)
        view.close()
    return  load_path



if __name__=='__main__':
    ux='http://pic.netbian.com/index.html'
    root_url(ux)
    #url = 'http://pic.netbian.com/index_10.html'
    #save_url(url)


```

## 壁纸设置
set_black.py
这里你可能已经注意到了这里导入了pil这个库，是的这里要实现的就是壁纸的预览，在tkinter窗口显示。
效果图就不放了，感兴趣的去**我先前写的博客看看**。爬虫代码如下：

```python

import urllib.request
import os
import re

def root_url(url):
    try:
        url=url
        headers={'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Mobile Safari/537.36 SE 2.X MetaSr 1.0'}
        respon=urllib.request.Request(url=url,headers=headers)

        reason=urllib.request.urlopen(respon)
        reason=reason.read().decode('gbk')
        path_main='</b></a></li><li><a href="(.*?)" title='
        path_view='target="_blank"><span><img src="(.*?)" alt='
        path_download='<a href="" id="img"><img src="(.*)" data-pic="'
        path_download=re.compile(path_download,re.M)

        path_main=re.compile(path_main,re.M)
        path_view=re.compile(path_view,re.M)

        path_main=path_main.findall(reason)
        path_view=path_view.findall(reason)
        main_url = []
        #print(path_main)


        u_='http://pic.netbian.com'
        view_url=[]
        download_url=[]

        for i in path_main:
            u=u_+i
            main_url.append(u)
        for i in path_view:
            v=u_+i
            view_url.append(v)
        view_url.remove(view_url[0])
        for i in main_url:
            req=urllib.request.Request(url=str(i),headers=headers)
            reason_=urllib.request.urlopen(req)
            reason_=reason_.read().decode('gbk')
            u_l=path_download.findall(reason_)[0]
            ul=u_+u_l

            download_url.append(ul)
        way=r'D:\time _ show\time _ show\data'
        if not os.path.exists(way):
            os.makedirs(way)
        with open(r'D:\time _ show\time _ show\data\view_url.hly','w',encoding='utf-8') as f :
            f.write(str(view_url))
            f.close()
        with open(r'D:\time _ show\time _ show\data\download_url.hly','w',encoding='utf-8') as f :
            f.write(str(download_url))
            f.close()
            #print(download_url)

    except Exception as e:
        pass
    
    
def save_url(url):
    way = r'D:\time _ show\time _ show\data\exit'
    if not os.path.exists(way):

        urx = 'http://pic.netbian.com/index.html'
        root_url(urx)
        os.makedirs(way)

    headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Mobile Safari/537.36 SE 2.X MetaSr 1.0'}
    respon = urllib.request.Request(url=url, headers=headers)
    reason = urllib.request.urlopen(respon)
    reason = reason.read().decode('gbk')
    path_main = '</b></a></li><li><a href="(.*?)" target="_blank">'
    path_view = ' target="_blank"><img src="(.*?)" alt='
    path_download = '<a href="" id="img"><img src="(.*)" data-pic="'
    path_download = re.compile(path_download, re.S)
    path_main = re.compile(path_main, re.M)
    path_view = re.compile(path_view, re.M)
    path_main = path_main.findall(reason)
    path_view = path_view.findall(reason)
    main_url = []
    #print(path_main)
    #print(path_view)

    m_v=open(r'D:\time _ show\time _ show\data\view_url.hly','r',encoding='utf-8')
    mv=m_v.read()
    m_v.close()
    mv_={}
    view_url=eval(mv,mv_)
    m_l = open(r'D:\time _ show\time _ show\data\download_url.hly', 'r', encoding='utf-8')
    ml=m_l.read()
    m_l.close()
    ml_={}
    download_url=eval(ml,ml_)

    u_ = 'http://pic.netbian.com'
    for i in path_main:
        u = u_ + i

        main_url.append(u)
    for i in path_view:
        v = u_ + i
        view_url.append(v)
    view_url.remove(view_url[0])
    for i in main_url:
        req = urllib.request.Request(url=str(i), headers=headers)
        reason_ = urllib.request.urlopen(req)
        reason_ = reason_.read().decode('gbk')
        u_l = path_download.findall(reason_)[0]
        ul = u_ + u_l
        download_url.append(ul)
    with open(r'D:\time _ show\time _ show\data\view_url.hly', 'w', encoding='utf-8') as f:
        f.write(str(view_url))
        f.close()
    with open(r'D:\time _ show\time _ show\data\download_url.hly', 'w', encoding='utf-8') as f:
        f.write(str(download_url))
        f.close()
        print(len(download_url))



def load_view(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Mobile Safari/537.36 SE 2.X MetaSr 1.0'}
    reqs=urllib.request.Request(url=url,headers=headers)
    pic=urllib.request.urlopen(reqs)
    pic=pic.read()
    way=r'D:\time _ show\picture\view'
    if not os.path.exists(way):
        os.makedirs(way)
    with open(r'D:\time _ show\picture\view\view.jpg','wb') as view:
        view.write(pic)
        view.close()

def load_down(url,name):
    headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Mobile Safari/537.36 SE 2.X MetaSr 1.0'}
    reqs=urllib.request.Request(url=url,headers=headers)
    pic=urllib.request.urlopen(reqs)
    pic=pic.read()
    way = r'D:\time _ show\picture\download'
    if not os.path.exists(way):
        os.makedirs(way)

    load_path_=r'D:\time _ show\picture\download\{}.jpg'
    load_path=load_path_.format(str(name))
    if not os.path.exists(way):
        os.makedirs(way)
    with open(load_path,'wb') as view:
        view.write(pic)
        view.close()
    return  load_path



if __name__=='__main__':
    ux='http://pic.netbian.com/index.html'
    root_url(ux)
    #url = 'http://pic.netbian.com/index_10.html'
    #save_url(url)





```
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200625230043684.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0ZVVEVST1g=,size_16,color_FFFFFF,t_70)
之后你看到的就是这个样子。
## 计时器天气显示
weather.py
说完了控制器，再回来说说计时器；
如图：
‘![在这里插入图片描述](https://img-blog.csdnimg.cn/20200625230225409.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0ZVVEVST1g=,size_16,color_FFFFFF,t_70)
在这上面又有一个天气显示，没错这也是一个爬虫。

```python
import urllib.request
import re


def weather():
    html = urllib.request.urlopen(r'http://www.weather.com.cn/weather/101240701.shtml',timeout=5)
    urllib.request.urlcleanup()
    read = html.read().decode('utf-8')

    def get_way(path, string):
        path_way = path
        path_get = re.compile(path_way)
        ture_key = path_get.findall(string, re.M)
        return str(ture_key)

    path_html = '<input type="hidden" id="hidden_title" value=".*"'
    see_html = get_way(path_html, read)
    path_see = 'v.*°C'
    see_weather = get_way(path_see, see_html)
    day = get_way('.*日', see_weather).strip('[\"\']')
    weather = get_way('周.*°C', see_weather).strip('[\']')
    #print(weather)
    return weather

if __name__ =='__main__':
    weather()


```
## 数据处理
两个软件之间是少不了数据交流的，这里用了一个最简单的办法，让两个软件去调用一个区域内的数据文件。
**不过我这里偷了个懒。**
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200625230616357.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0ZVVEVST1g=,size_16,color_FFFFFF,t_70)
可以看到我直接将数据写入成一个list，之后直接读取内容，使用eval()这个函数进行转换，这样做是不太正确的请大家注意一下！
## SUMMARY
最后这个项目就是这个样子的

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200625230949597.png)
具体的代码已经给出来了，大概就是这个样子。
