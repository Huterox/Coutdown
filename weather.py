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

