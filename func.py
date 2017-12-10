#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#函数本身也可以赋值给变量，即：变量可以指向函数。
f=abs
print(f(-10))	#f只想abs
#高阶函数也就是将函数变量作为参数传入函数中
def high_func(a,b,f):
 	print(f(a),"+",f(b))
#map。map()函数接收两个参数，一个是函数，一个是Iterable，
#map将传入的函数依次作用到序列的每个元素，并把结果作为新
#的Iterator返回。
#比如我们有一个函数f(x)=x2，要把这个函数作用在一个list 
#[1, 2, 3, 4, 5, 6, 7, 8, 9]上
def fx(x):
	return x*x
#返回函数，即返回值是一个函数并且每次返回的不是同一个。
def out_funct(*args):
	def sum():
		ax=0
		for i in args:
			ax=ax+i
		return ax
	return sum
#匿名函数，用关键字lambda表示
f=lambda x:x*x
print(list(map(lambda x:x*x,[1,2,3,4,5])))
#装饰器
#函数也是一个对象，而且函数对象可以被赋值给变量
#>> def now():...     print('2015-3-25')...>>> f = now>>> f()
#函数中的_name_属性可以获得函数的名字
def now():
	pass
#模块
#，每一个包目录下面都会有一个__init__.py的文件，
#这个文件是必须存在的，否则，Python就把这个目录当成普通目录，
#而不是一个包。__init__.py可以是空文件，也可以有Python代码，
#因为__init__.py本身就是一个模块，
# 任何模块代码的第一个字符串都被视为模块的文档注释；

