#!/usr/bin/python2.7
#coding=utf-8

'''
    assertion.py

    只占位，不消费的零宽断言：
    -- 没错，零宽断言就是个去麦当劳写作业的小学生～

    怎么查找在某些内容（但并不包括这些内容，否则你可以使用像电话号码匹配那样的
    if-else + 分组去实现）之前或之后的东西?
    即类似于\b ^ $这样的定位符，正则里这样的规则匹配称为（负向）? 零宽断言

    这个又分为两种，一种是(?=exp)这样的，也叫零宽度正预测先行断言，
    它断言自身出现的位置后面能匹配表达式exp，举个例子，匹配ing结尾的单词前半部分:
    \b\w+(?=ing\b)
    它会匹配中 I'm singing while you're dancing. 里的sing和danc

    另外一种即(?<=exp)也叫零宽度正回顾后发断言，即它断言自身出现的位置的前面
    能匹配表达式exp，举个例子：
    (?<=\bre)\w+\b
    这里匹配的是以re开头的单词的后半部分（再次强调，re本身不会算在内），比如
    reading a book 就会匹配ading

    负向零宽断言，显然的，便是 确保某个字符没有出现，而且不能匹配它，篇幅有限，
    不再赘述...

'''

import re

#test_case = "I'm singing while you're dancing."
test_case = "aaalllsss0tAAAnnn999"

#匹配3个连续相同字符前相邻的3个连续相同字符
m = re.findall(
    #3个需要匹配中的连续相同字符，使用分组实现！！
    r'(\w)\1{2}(?=(\w)\2{2})',
    #r'\b\w+(?=ing\b)',
    test_case)

if m:
    print m
