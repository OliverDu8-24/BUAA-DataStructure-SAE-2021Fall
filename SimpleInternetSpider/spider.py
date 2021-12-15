import urllib.request
from html.parser import HTMLParser
import pandas as pd
import openpyxl


class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.sheet = []
        self.row = []
        self.entry = []
        self.tr = False
        self.td = False
        self.p = False

    def handle_starttag(self, tag, attrs):
        if tag == 'tr':
            self.tr = True
            self.row = []
        elif tag == 'td':
            self.entry = []
            self.td = True
        elif tag == 'p':
            self.p = True

    def handle_endtag(self, tag):
        if tag == 'tr':
            self.tr = False
            self.sheet.append(self.row)
        elif tag == 'td':
            tmp = ''
            for i in self.entry:
                tmp += i
            self.row.append(tmp)
            self.td = False
        elif tag == 'p':
            self.p = False

    def handle_data(self, data):
        if self.tr and self.td and self.p:
            self.entry.append(data.strip())


if __name__ == '__main__':
    URL = 'http://10.212.30.136:8200/exam/piePass?id=713'

    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                            'Chrome/94.0.4606.71 Safari/537.36 Edg/94.0.992.38',
              'Cookie' : r'Hm_lvt_8edeba7d3ae859d72148a873531e0fa5=1632798454,1634379030; '
                         'vuex={"user":{"loginInfo":''{"username":"20376203","userId":360,'
                         '"token":"auth:360:e5cac643-e838-4b01-9191-7af65966bea8",'
                         '"role":1,"name":"陈俊一","courseName":"2021秋季课程"},'
                         '"remember":true,"hideGraph":false},'
                         '"discussion":{"lastPosition":0}}'
              }

    request = urllib.request.Request(URL, headers=header)
    re = urllib.request.urlopen(request).read()

    print(re)