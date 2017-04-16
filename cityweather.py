# -*- coding:utf8 -*-
import requests
while True:
    input_city = raw_input("请输入你要查询的城市: \n")
    if not input_city:
        break
    url = ('http://wthrcdn.etouch.cn/weather_mini?city=%s' % input_city)
    get_dict = requests.get(url)
    result = get_dict.json()
    result_data = result.get('data')
    if result_data:
        print '当前温度: ', result_data.get('wendu'), '°C'
        print '当前空气质量', result_data.get('aqi')
        print result_data.get('ganmao')
        print '5日天气预报: '
        forcast = result_data.get('forecast')
        for i in forcast:
            print i.get('date'), ': ', i.get('type'), ',', i.get('low'), ',', i.get('high')
    else:
        print '未能获取到该城市天气'
    print
