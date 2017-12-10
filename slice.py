#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#L[0:3]表示，从索引0开始取，直到索引3为
#止，但不包括索引3。即索引0，1，2，正好是3个元素
l=[1,2,3,4,5]
#slice也可以进行倒着进行切片
# 后10个数：L[-10:]
#前10个数，每两个取一个：L[:10:2]
print(l[2:3])
#列表生成式
a=list(range(1,11))#生成1到10的数字
# l=[]
# for i in range(1,11):
# 	l.append(i*i)
# print(l) 另一种方式
print([x*x for x in range(1,10)])
#两层嵌套
print([m+n for m in 'ABC' for n in 'ef'])
import os	#导入os模块
print([d for d in os.listdir('.')]) #列出文件和目录
#循环其实可以同时使用两个甚至多个变量，比如dict的items()
#可以同时迭代key和value：
 
# for k,v in d.items():
# 	print(k,"=",v)
#a.lower() 变成小写字母
L=["hello,Python","Ibm","oracle"]
print([s.lower() for s in L])
#使用列表生成式来写
d={'x':'A','y':'B','z':'C'}
print([m+'='+n for m,n in d.items()])
from collections import Iterable
print(isinstance('aa',Iterable))