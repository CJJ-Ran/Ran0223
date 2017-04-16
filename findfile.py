# coding:utf-8
import os
import os.path


def find(x):
    s = []
    for root, dir, filename in os.walk('.'):
        for j in filename:
            path = root+'\\'+j
            if x in path:
                s.append(path)
            with open(path) as f:
                for k in f.readlines():
                    if x in k:
                        s.append(path+':'+k)
    return s
while True:
    keyword = raw_input('输入关键字:\n')
    if keyword:
        folder = find(keyword)
        for t in folder:
            print t
    else:
        break
