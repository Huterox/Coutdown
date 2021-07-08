
import tkinter.messagebox
import os

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

        self.win=tkinter.Tk()
        self.win.geometry('600x300')
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
        tkinter.messagebox.showinfo('tips','此版本为校园版（删减版）\nQ3139541502获取完整版\n68元可获取全套python或C++学习资源\n附加软件源码')


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
        self.Button_link = tkinter.Button(self.win, font=('宋体', 14), text='版本信息', relief='groove',command=lambda :Win.link_author(self))

        self.Button_link.place(x=240, y=175, width=200, height=25)

    def mainloop(self):
        self.win.mainloop()



if __name__=='__main__':

    win=Win()
    win.Label()
    win.Entry()
    win.Button()

    win.mainloop()

