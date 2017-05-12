# 通过HTTP请求和XML实现获取电视节目
# API：http://www.webxml.com.cn/webservices/ChinaTVprogramWebService.asmx

import requests
from xml.etree import ElementTree as ET

def print_city():
    city = requests.get('http://www.webxml.com.cn/webservices/ChinaTVprogramWebService.asmx/getAreaDataSet')
    root = ET.XML(city.text)
    areaID, Area = [], []
    for id in root.iter('areaID'):
        areaID.append(id.text)
    for node in root.iter('Area'):
        Area.append(node.text)
    for i in range(len(areaID)):
        print('频道ID: {}  ->  {}'.format(areaID[i], Area[i]))

def select_dianshitai(iD):
    dianshitai = requests.get('http://www.webxml.com.cn/webservices/ChinaTVprogramWebService.asmx/getTVchannelDataSet?'
                              'theTVstationID={}'.format(iD))
    root = ET.XML(dianshitai.text)
    tvChannelID, tvChannel = [], []
    for tvID in root.iter('tvChannelID'):
        tvChannelID.append(tvID.text)
    for tvCH in root.iter('tvChannel'):
        tvChannel.append(tvCH.text)
    for i in range(len(tvChannelID)):
        print('频道号: {} -> {}'.format(tvChannelID[i], tvChannel[i]))

# def select_pindao():
#     pindao = requests.get('http://www.webxml.com.cn/webservices/ChinaTVprogramWebService.asmx/getTVchannelString?'
#                           'theTVstationID=10')
#     print(pindao.text)

def tv_list():
    final = requests.get('http://www.webxml.com.cn/webservices/ChinaTVprogramWebService.asmx/getTVprogramDateSet?'
                         'theTVchannelID=1&theDate=2017-05-11&userID=')
    print(final.text)

if __name__ == '__main__':
    print_city()
    iD = input('请输入ID: ')
    select_dianshitai(iD)
