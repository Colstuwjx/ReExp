#!/usr/bin/python2.7
#coding=utf-8

'''
    comment_greedy_laze.py
    如果一个正则表达式过于复杂，我们能不能想办法加下注释呢? 
    答案是肯定的! 正则表达式提供comment定义用以指定一些需要
    忽略的，无需解析的字符串，语法是：

    #没错! 用分组来做到!
    (?#comment)

    当然，在py里这个特性比较鸡肋，我们可以用更可读的方式实现注释.

    除此之外，元字符的匹配里，一个特殊的字符对便是.*
    我们常常会困惑它到底匹配了多少部分，这便是你需要了解的一个概念：
    贪婪匹配和懒惰匹配.

'''

import re
 
html = 'Hello <a href="http://pypix.com" title="pypix">Pypix</a>' \
       'Hello <a href="http://example.com" title"example">Example</a>'
 
#m = re.findall('<a.*>.*<\/a>', html)
m = re.findall('<a.*?>.*?<\/a>', html)

if m:
    print m