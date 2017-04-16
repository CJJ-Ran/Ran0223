# -*-coding:utf8-*-
import re

with open('from.txt') as f:
    word_lst = f.readlines()
    word_str = ' '.join(word_lst)
    pattern = re.compile(r'\b[A-z]\S+[A-z]\b')
    word_en = pattern.findall(word_str)
result = sorted(word_en, key=lambda x: x[0])
with open('to.txt', 'a') as g:
    for i in result:
        g.write(i + '\n')
