#!/usr/bin/python2.7
#coding=utf-8

'''
    meta_repeat_strcls.py
    正则表达式通过元字符、重复、字符类等方式实现模糊和重复字符匹配；
    *   重复零次或更多次
    +   重复一次或更多次
    ?   重复零次或一次
    {n} 重复n次
    {n,}    重复n次或更多次
    {n,m}   重复n到m次

    .   匹配除换行符以外的任意字符
    \w  匹配字母或数字或下划线或汉字
    \s  匹配任意的空白符
    \d  匹配数字
    \b  匹配单词的开始或结束
    ^   匹配字符串的开始
    $   匹配字符串的结束
    像'(' ')'等自身不包含意义，而还有很多和字符集有关，比如匹配unicode的一些元字符等.


'''

import re
 
phone_numbers = [ "(010)88886666",
        "022-22334455",
        "02912345678",
        "010)12345678",
        "(022-87654321" ]
 
for pn in phone_numbers:
    pattern = re.match(r"\(?0\d{2}[) -]?\d{8}", pn)
 
    if pattern:
        print '{0} is valid phone number.'.format(pn)
    else:
        print '{0} is not valid phone number.'.format(pn)
