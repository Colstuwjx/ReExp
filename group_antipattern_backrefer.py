#!/usr/bin/python2.7
#coding=utf-8

'''
    group_antipattern.py
    正则表达式的分组是使用频率相当高的一个特性，
    它用来获取指定匹配成功的一组字符串信息，
    而你可以灵活的指定不捕获组或是加上命名以更快捷的找到特定组别；

    正则还提供反义即反选的功能，这也是非常常见的需求，比如我需要
    找到没被注释的配置内容，那么就是一个[^#]，这也是反义的一个应用；
    常用的反义代码有以下几个：
    \W			匹配任意不是字母，数字，下划线，汉字的字符
	\S			匹配任意不是空白符的字符
	\D			匹配任意非数字的字符
	\B			匹配不是单词开头或结束的位置
	[^x]		匹配除了x以外的任意字符
	[^aeiou]	匹配除了aeiou这几个字母以外的任意字符

	指定了分组之后，如何在后续匹配正则里引用它呢?
	正则提供了后向引用的概念，你可以在后续字符串中使用组号或者组名来命中（不捕获的组别无法定位）
	举个例子， \b(\w+)\b\s+\1\b 这里便是用\1来匹配前面匹配中的单词，意义便是匹配重复单词，比如go go
    引用命名组也很简单：\b(?<Word>\w+)\b\s+\k<Word>\b

'''

import re          

string = 'Hello foobar'         
pattern = re.search(r'(f.*)(b.*)', string)          
#pattern = re.search(r'(H.*)(f.*)(b.*)', string)    

#在分组最开始加上?:即意味着不捕获分组标记，re模块不会记入分组，但是匹配仍然奏效      
#pattern = re.search(r'(?:H.*)(f.*)(b.*)', string)          

#你还可以通过给匹配组命名的方式来强化获取方式
#并且你惊讶的发现，group 0 1 的方式仍然奏效!!
pattern = re.search(r'(?P<fstar>f.*)(?P<bstar>b.*)', string)

#print "[named] f* => {0}".format(pattern.group('fstar')) 
# prints f* => Hello          
#print "[named] b* => {0}".format(pattern.group('bstar')) 
# prints b* => bar

print "f* => {0}".format(pattern.group(1)) 
# prints f* => Hello          
print "b* => {0}".format(pattern.group(2)) 
# prints b* => bar