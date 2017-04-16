# coding:utf8
import random


def xipai():
    lst1 = ['joker','JOKER']
    lst2 = ['HX','HT','MH','FK']
    lst = []
    for i in lst2:
        for j in range(1,14):
            k=i+'%d' %j
            lst.append(k)
    lst.extend(lst1)
    random.shuffle(lst)
    return lst


def fapai():
    for i in range(0,50,3):
        A.append(lst[i])
        B.append(lst[i+1])
        C.append(lst[i+2])
    D=lst[-3:]
    print '玩家A：',A
    print '玩家B：',B
    print '玩家C：',C
    print '底牌D：',D
i = 1
while i:
    A = []
    B = []
    C = []
    D = []
    play = input('开始游戏:1，退出游戏:0:\n')
    if play:
        lst = xipai()
        fapai()
    else:
        i = 0
print '游戏结束!'
