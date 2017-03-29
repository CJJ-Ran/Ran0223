# -*-coding:utf8-*-
import requests
import sys
from city import city
reload(sys)
sys.setdefaultencoding('utf-8')
try:
    while True:
        city_name = raw_input('输入你要查询的城市：\n')
        if not city_name:
            break
        if city_name in city.keys():
            city_num = city.get(city_name)
            url = 'http://www.weather.com.cn/data/cityinfo/101%s.html' % city_num
            result = requests.get(url)
            data = result.json()
            results = data['weatherinfo'].values()
            cityname = results[0].encode('raw_unicode_escape')
            weather = results[5].encode('raw_unicode_escape')
            temp2 = results[3].encode('raw_unicode_escape')
            temp1 = results[4].encode('raw_unicode_escape')
            print """城市：%s
天气：%s
最高气温：%s
最低气温：%s
""" % (cityname, weather, temp2, temp1)
        else:
            print "没有该城市天气预报"
except:
    print "网页请求错误！"
