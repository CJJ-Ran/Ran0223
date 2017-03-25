# -*-coding:utf8-*-
import time # 调用时间模块


def read_data(x, data_index=None):  # 定义读取历史数据函数
    data_detail = []
    with open(x) as f:
        form = f.readlines()
        for form_detail in form:
            detail = form_detail.strip().split(' ')
            j = 1
            for k in detail[1:data_index]:
                detail[j] = int(k)
                j += 1
            data_detail.append(detail)
    return data_detail


def check_one(one):     # 定义查询最近10笔交易记录函数
    print '最近十笔交易'
    record_name = ['交易对象', '收入', '支出', '应收账款', '应出账款', '交易日期']
    check_record = read_data(one, data_index=-1)
    print '  '.join(record_name)
    for i in range(1, 11):
        check_account = check_record[-i]
        for j in range(len(check_account)):
            check_account[j] = str(check_account[j])
        check_data = '\t'.join(check_account)
        print '  ' + check_data


def check_two(two):     # 定义查询与某家公司交易往来函数
    company_name = raw_input('请输入公司名：')
    record_name = ['交易时间：', '收入：', '支出：', '应收账款：', '应出装款：']
    company_record = read_data(two, data_index=-1)
    check_record = []
    for i in company_record:
        check_record.append(i[0])
    if company_name in check_record:
        company_data = []
        j = 0
        for i in check_record:
            if i == company_name:
                company_data.append(company_record[j][1:])
            j += 1
        print
        print '与 %s 共有 %d 笔交易' % (company_name, len(company_data))
        for i in company_data:
            for j in range(len(i)):
                if j == 0:
                    print record_name[j] + i[-1]
                else:
                    print record_name[j] + str(i[j-1]) + '万'
            print
    else:
        print "与 %s 暂无交易" % company_name


def check_three(three):     # 定义查询最新资产-债务函数
    new_record = ['最新资产：', '最新负债：', '最新净资产：', '最后更新时间：']
    new_data = read_data(three)
    for i in range(len(new_data[-1])):
        if i == 0:
            print new_record[-1] + new_data[-1][i]
        else:
            print new_record[i - 1] + str(new_data[-1][i]) + '万'
    print


def record(debt):       # 定义记账函数
    sort_name = ['交易对象：', '收入/万：', '支出/万：', '应收账款/万：', '应出账款：', '交易日期：']
    asset_name = ['结算日期', '最新资产:', '最新负债：', '最新净资产:']
    latest_asset = [0, 0, 0, 0]
    new_bill = [0, 0, 0, 0, 0, 0]
    print "记账模式"
    for i in range(5):
        if i == 0:
            new_bill[i] = raw_input(sort_name[i])
        else:
            type_decide = raw_input(sort_name[i])
            if type_decide.isdigit():
                new_bill[i] = int(type_decide)
                decide_result = True
            else:
                decide_result = False
                break
    if decide_result:
        new_bill[-1] = time.strftime('%m月%d日', time.localtime(time.time()))
        print '%s%s' % (sort_name[-1], new_bill[-1])
        liabilities = read_data(debt)
        latest_asset[1] = int(liabilities[-1][1]) + int(new_bill[1]) - int(new_bill[2])
        latest_asset[2] = int(liabilities[-1][2]) + int(new_bill[4]) - int(new_bill[3])
        latest_asset[3] = latest_asset[1] - latest_asset[2]
        latest_asset[0] = time.strftime('%m月%d日', time.localtime(time.time()))
        print
        print "交易已记录\n当前资产状况："
        for i in range(1, 4):
            print asset_name[i] + str(latest_asset[i]) + '万'
        write_data('liabilities.txt', latest_asset)
        write_data('journal_account.txt', new_bill)
        print
    else:
        print "数据类型非法，无法录入，请重新选择服务"


def write_data(x, new_data):        #定义资产-债务更新函数
    with open(x, 'a') as f:
        for i in range(len(new_data)):
            new_data[i] = str(new_data[i])
        data_str = ' '.join(new_data)
        f.write(data_str + '\n')


def choose_service():               # 定义服务选择主程序函数
    user_choose = True
    user_choose1 = raw_input('1.查账，2.记账,3.退出服务\n请选择服务\n')
    while user_choose:
        if user_choose1 == '1':     # 查账模式
            print """查账模式
1.查询最近十笔交易记录
2.查询与某公司交易往来
3.查询最近资产负债状况
返回上一层请按Enter键"""
            user_choose2 = raw_input("请选择服务:\n")
            choose_decide = True
            while choose_decide:
                if user_choose2 == '1':     # 查询最近十笔交易记录
                    check_one('journal_account.txt')
                    user_choose1 = '1'
                    break
                elif user_choose2 == '2':   # 查询与某公司交易往来
                    check_two('journal_account.txt')
                    user_choose1 = '1'
                    break
                elif user_choose2 == '3':   # 查询最近资产负债状况
                    check_three('liabilities.txt')
                    user_choose1 = '1'
                    break
                elif not user_choose2:      # 返回上一层请按Enter键
                    user_choose1 = raw_input("1.查账，2.记账,3.退出服务\n请选择服务\n")
                    break
                else:                       # 异常判断
                    print """"
服务选择错误，请重新选择服务
查账模式
1.查询最近十笔交易记录
2.查询与某公司交易往来
3.查询最近资产负债状况
返回上一层请按Enter键"""
                    user_choose2 = raw_input('')
                    if not user_choose2:
                        user_choose1 = raw_input("1.查账，2.记账,3.退出服务\n请选择服务\n")
                        break
        elif user_choose1 == '2':   # 记账模式
            record('liabilities.txt')
            user_choose1 = raw_input('1.查账，2.记账,3.退出服务\n请选择服务\n')
        elif user_choose1 == '3':   # 退出服务
            user_choose = False
        else:                       # 判断异常
            print """
服务选择错误，请重新选择
1.查账，2.记账,
退出服务请直接按Enter键"""
            user_choose1 = raw_input('')
            if not user_choose1:
                user_choose = False

try:        # 异常判断
    choose_service()
except:
    print '数据异常'
