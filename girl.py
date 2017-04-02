# -*-coding:utf8-*-
import requests
import re
import threading
import os
from time import ctime


def page_choose(homepage):      # 定义页码选择函数
    start_page = '起始页码page_num1='
    print start_page,
    page_num1 = page_examine(homepage-1, start_page)
    end_page = '结束页码page_num2='
    print end_page,
    page_num2 = page_examine(homepage, end_page, minpage=page_num1+1)
    return page_num1, page_num2


def page_examine(maxpage, page_num, minpage=0):     # 定义输入页码是否规范有效函数
    page = raw_input()
    decide = True
    while decide:
        if not (page.isdigit() and int(page) in range(minpage, maxpage)):
            page = raw_input('页码输入错误，请重新输入\n%s' % page_num)
        else:
            return int(page)
            decide = False


def max_page():     # 定义抓取妹纸图最大页码函数
    url = 'http://jandan.net/ooxx'
    response = requests.get(url)
    home_page = response.content
    pattern = re.compile(r'page-(\d+)')
    page_num = pattern.findall(home_page)
    home_page_num = max([int(x) for x in page_num])
    print "目前共有0-%d页妹纸图可供选择\n请在0-%d范围内选择你要下载的妹纸图页码区间" % (home_page_num, home_page_num)
    return home_page_num


def MM_url(page1, page2):       # 定义抓取妹纸图链接函数
    all_page = ''
    pattern = re.compile(r'//\w+.sinaimg.cn/large/\w*.jpg')
    for i in range(page1, page2):
        url_page = 'http://jandan.net/ooxx/page-%d#comments' % i
        all_page += (requests.get(url_page)).content
    mm = pattern.findall(all_page)
    return mm


def folder():       # 定义妹纸图保存地址
    folder_name = 'mm'
    os.mkdir(os.path.join('', folder_name))
    meizhi_path = '.\\' + folder_name + '/'
    return meizhi_path


def meizhi(url_list, mm_path):      # 定义妹纸图下载并保存函数
    count = 1
    print '共找到%d张妹纸图片，现在开始下载' % len(url_list)
    for i in url_list:
        print '第%d张妹纸图已下载成功' % count
        with open(mm_path+str(count)+'.jpg', 'wb') as f:
            f.write((requests.get('http:' + i)).content)
        count = int(count) + 1
# 主程序
try:
    user_choose_page = page_choose(max_page()+1)        # 选择页码区间
    mm_url = MM_url(user_choose_page[0], user_choose_page[1])   # 获得妹纸图基本链接信息
    threads = []
    t = threading.Thread(target=meizhi, args=(mm_url, folder()))    # 多线程抓取
    threads.append(t)
except:
    print '程序异常，无法使用。'
if __name__ == '__main__':  # 调用主程序并运行
    for i in threads:
        i.setDaemon(True)   # 声明守护线程
        i.start()           # 开始线程活动

    i.join()                # 阻塞主线程，保证所有子线程都能完全运行结束
    print "over %s" % ctime()
