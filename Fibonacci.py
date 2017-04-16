# -*- coding:utf8 -*-
num_lst = [1, 1]
ans = raw_input('输入一个大于3的整数：')
if ans.isdigit():
    ans = int(ans)
    if ans > 3:
        for i in range(ans):
            num_lst.append(num_lst[i]+num_lst[i+1])
        for i in num_lst:
            print i
    else:
        print '输入错误'
else:
    print '输入错误'
