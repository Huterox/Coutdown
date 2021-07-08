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









































