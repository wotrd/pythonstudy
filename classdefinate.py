#!/usr/bin/env python3
# -*- coding:utf-8 -*-

class Student(object):
	__slots__=('name')
	def __init__(self,name):
		self.name=name

class Student(object):
	def set_name(self,value):
		self.name=value
f=Student('xioawnag')
f.age=24
print(f.age)
#除了使用type()动态创建类以外，要控制类的创建行为，
#还可以使用metaclass。
#打开文件的函数open()，成功时返回文件描述符
#（就是一个整数），出错时返回-1
