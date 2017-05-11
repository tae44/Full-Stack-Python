# 通过HTTP请求和XML实现获取电视节目
# API：http://www.webxml.com.cn/webservices/ChinaTVprogramWebService.asmx

import requests
from xml.etree import ElementTree as ET

def print_city():
    city = requests.get('http://www.webxml.com.cn/webservices/ChinaTVprogramWebService.asmx/getAreaString')
    root = ET.XML(city.text)
    print(city.text)
    for node in root.tag:
        print(node)

def select_dianshitai():
    dianshitai = requests.get('http://www.webxml.com.cn/webservices/ChinaTVprogramWebService.asmx/getTVstationString'
                              '?theAreaID=1')
    print(dianshitai.text)

def select_pindao():
    pindao = requests.get('http://www.webxml.com.cn/webservices/ChinaTVprogramWebService.asmx/getTVchannelString?'
                          'theTVstationID=2')
    print(pindao.text)

def tv_list():
    final = requests.get('http://www.webxml.com.cn/webservices/ChinaTVprogramWebService.asmx/getTVprogramDateSet?'
                         'theTVchannelID=1&theDate=2017-05-11&userID=')
    print(final.text)

if __name__ == '__main__':
    print_city()
