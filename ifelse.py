#!/usr/bin/python2.7
#coding=utf-8

'''
    ifelse.py
    正则表达式甚至可以做到if-else逻辑判断，格式如下:
    regex a|regex b    #单纯或的模式
    (?(?=regex)then|else)    #if-else选择模式
    
    刚才电话号码的情况, 会匹配到一些错误格式的字符串, 
    这便可以通过if-else判断来解决.
'''

import re
 
phone_numbers = [ "(010)88886666",
        "022-22334455",
        "02912345678",
        "010)12345678",
        "(022-87654321" ]
 
for pn in phone_numbers:
    #pattern = re.match(r"\(?0\d{2}[) -]?\d{8}", pn)
    #pattern = re.match(r"\(?0\d{2}\)?[-]?\d{8}|0\d{2}[-]?\d{8}", pn)
    pattern = re.match(r"(\()?0\d{2}(?(1)\)|)[-]?\d{8}", pn)
 
    if pattern:
        print '{0} is valid phone number.'.format(pn)
    else:
        print '{0} is not valid phone number.'.format(pn)
