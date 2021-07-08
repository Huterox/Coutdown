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
        self.win.resizable(width=False,height=False)
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
        set_time(00,00,00,7,self.month,2020)
    def command_day(self):
        self.day=str(self.entry_day.get())
        set_time(00,00,00,self.day,7,2020)
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

