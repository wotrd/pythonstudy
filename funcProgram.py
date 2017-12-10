#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#函数本身也可以赋值给变量，即：变量可以指向函数。
f=abs
print(f(-10))	#f只想abs
#高阶函数也就是将函数变量作为参数传入函数中
def high_func(a,b,f):
 	print(f(a),"+",f(b))
	