#!/usr/bin/env python3
# -*- coding: utf-8 -*-\
def nop():
	pass	#缺少了pass代码就会有语法错误

def myAbs(x):
	if x>=0:
		return x
	else:
		return -x
# calc(*nums)表示将nums中的所有元素加入进去
#可变参数允许你传入0个或任意个参数
#**extra表示把extra这个dict的所有key-value用关键字
#参数传入到函数的**kw参数，kw将获得一个dict，
#注意kw获得的dict是extra的一份拷贝，对kw的改动
#不会影响到函数外的extra
#命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
def person(name,age,city='jiann',job='engineer'):
	print (name,age,city,job)
#定义默认参数要牢记一点：默认参数必须指向不变对象！

# def add_end(L=None):
# 	if L is None:
# 		L=[]
# 		L.append("END")
# 		return L
def calc(numbers):
	sum = 0
	for n in numbers:
		sum=sum+n*n
	return sum
# 把函数的参数改为可变参数：
def calcu_1(*numbers):
	sum=0
	for i in numbers:
		sum=sum+i*i
	return sum
#关键字参数可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。而关键字参数允许
#你传入0个或任意个含参数名的参数，这些关键字参数在
#函数内部自动组装为一个dict
def antic_method(name,age,**kw):
	print("name:",name,"age:",age,"other:",kw)
#如果函数定义中已经有了一个可变参数，后面跟着的
#命名关键字参数就不再需要一个特殊分隔符*了：
#可以用必选参数、默认参数、可变参数、关键字
#参数和命名关键字参数，这5种参数都可以组合使用。
#递归函数
def fact(num,product):
	if num==1:
		return product
	else:
		return fact(num-1,product*num)

# def get_jishu():
# 	l=[]
# 	for index in range(1,100):
# 		if index%2!=0:
# 			l.append(index)
# 	print (l)	
def get_jishu_1():
	i=1
	l=[]
	while i<=99:
		l.append(i)
		i=i+2
	print(l)