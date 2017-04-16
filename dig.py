# -*- coding:utf8 -*-
def dig(x=5, y=5, z="*"):
    for i in range(x):
        for j in range(y):
            print z,
        print
dig()
dig(x=3, y=3)
dig(x=3, y=3, z="!")
