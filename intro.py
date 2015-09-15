#!/usr/bin/python2.7
#coding=utf-8

'''
    intro.py
    怎样校验一个字符串是否符合电子邮箱地址的规则?
    怎样去快速的搜索和切分字符串?
    怎样去得到格式化的数据?

    让我们试试正则表达式吧!!!
'''

import re
 
mails = [ "www.baidu.com",
        "1@qq.com.",
        "1.@qq.com",
        "1@qq.com.",
        "mail@qq.com" ]
 
for mail in mails:
    #pattern = re.match(r"^[\w!#$%&'*+/=?^_`{|}~-]+(?:\.[\w!#$%&'*+/=?^_`{|}~-]+)*@(?:[\w](?:[\w-]*[\w])?\.)+[\w](?:[\w-]*[\w])?$", mail, re.DEBUG)
    pattern = re.match(r"^[\w!#$%&'*+/=?^_`{|}~-]+(?:\.[\w!#$%&'*+/=?^_`{|}~-]+)*@(?:[\w](?:[\w-]*[\w])?\.)+[\w](?:[\w-]*[\w])?$", mail)

    if pattern:
        print '{0} is valid mail address'.format(mail)
    else:
        print '{0} is not valid mail address'.format(mail)
