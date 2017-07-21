# 通过HTTP请求和JSON实现获取天气状况
# API：http://wthrcdn.etouch.cn/weather_mini?city=北京

import requests
import json

ret = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=北京')

w = json.loads(ret.text, encoding='utf-8')

f = w['data']['forecast']

print('当前温度: {}度'.format(w['data']['wendu']))
print('感冒几率: {}'.format(w['data']['ganmao']))
print('{}天气情况: 风向 -> {} , 风力 -> {} , 最高温度 -> {} , 最低温度 -> {}'.format(f[0]['date'], f[0]['fengxiang'],
                                                                       f[0]['fengli'], f[0]['high'], f[0]['low']))
print('{}天气情况: 风向 -> {} , 风力 -> {} , 最高温度 -> {} , 最低温度 -> {}'.format(f[1]['date'], f[1]['fengxiang'],
                                                                       f[1]['fengli'], f[1]['high'], f[1]['low']))
