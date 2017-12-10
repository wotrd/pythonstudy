#!/usr/bin/env python3
#-*- coding: utf-8  -*-
#ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符：
ord('A')
ord('中')
chr(66)
chr(25991)
#如果知道字符的整数编码，还可以用十六进制这么写str：网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes。

#Python对bytes类型的数据用带b前缀的单引号或双引号表示：
x = b'ABC'
#要注意区分'ABC'和b'ABC'，前者是str，后者虽然内容显示得和前者一样，
#但bytes的每个字符都只占用一个字节。
#以Unicode表示的str通过encode()方法可以编码为指定的bytes, 
'ABC'.encode('ascii')
b'ABC'
'中文'.encode('utf-8')
#要计算str包含多少个字符，可以用len()函数：
len('ABC')

#len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数

print ("niaho","ggg","ggggafa",100+300) 
name = input("请输入")		#输入语句
# Python还允许用r''表示''内部的字符串默认不转义，
print (r"///n","niggggg")
print ("name=",name)
#可以在input中加上提示字符
# python使用缩进区别代码块，一般为4个空格

#Python允许用'''...'''的格式表示多行内容，
print(r'''nihao
hello
ggg''')

#空值是Python里一个特殊的值，用None表示。None不能理解为0，
#因为0是有意义的，而None是一个特殊的空值。此外，
#Python还提供了列表、字典等多种数据类型，
#还允许创建自定义数据类型，我们后面会继续讲到。
#同一个变量可以反复赋值，而且可以是不同类型的变量


a=0
if a>=10:
	print("niaho")
	  #占位符什么也不做，用于充当没写完的函数代码
else:
	print("failed")
exit()  #结束语句#号为注释字符