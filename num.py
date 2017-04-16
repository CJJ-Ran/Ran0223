# -*- coding: utf8 -*-
# 1,2,3,4四个数字中的任意
# 三个组成的三位数及总个数
a = 0
for i in range(1, 5):
   for j in range(1, 5):
      for k in range(1, 5):
         if i == j or j == k or i == k:
            continue
         else:
            print "%d%d%d" % (i, j, k)
            a += 1
print a
