
# -*- coding:utf8 -*-
import re
import string


def word(x):
    with open(x, 'r') as f:
        word_lst = [i.strip().decode('utf8') for i in f.readlines()]
        return word_lst


def inspects(x):
    word_str = x
    pattern = re.compile(r'\b[A-z]\S+[A-z]\b')
    letter = pattern.findall(word_str)
    word_lst = []
    for i in word_str:
        if i not in list(string.letters):
            word_lst.append(i)
        elif i in word_str.split(' '):
            word_lst.append(i)
    word_lst += letter
    for i in word_lst:
        if i in word('lexicon.txt'):
            word_lst[word_lst.index(i)] = len(i) * '*'
    word_lst = [i for i in word_lst if i != u' ']
    print ' '.join(word_lst)
while True:
    x = raw_input('输入文字(直接回车退出)：\n')
    x = x.decode('utf8')
    if not x:
        break
    str2 = word('lexicon.txt')
    inspects(x)
