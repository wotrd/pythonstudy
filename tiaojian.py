#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# if x:
#     print('True')
# a=1 if为非0数值，非空字符串，非空list就判断为true，反之为false 
a = input('请输入birth')
b=int(a)
if b>2000:
	print('00后')
	pass
elif (b<3): #括号加不加都可以
	print('00前')
else:
	print('budayu')
#循环语句
#for循环可以遍历列表或者字符串
for letter in 'Python':
	print('当前字母:',letter)
	pass
fruits = ['fruit','banana','pear']
for fruit in fruits:
	print('fuit is:',fruit)
	pass
#通过序列进行迭代
for x in range(5,10):
	print("x=",x)
	pass
for index in range(len(fruits)):
	print("index",fruits[index],"is")
	pass
for num in range(10,20): #迭代10到20之间的数字
	for i in range(2,num) : #根据因子迭代
		if num%i ==0:	#确定第一个因子
			j=num/i
			print('%d 等于 %d * %d' %(num,i,j))
			break #退出当前循环
	else:	#注意缩进，对应不同得到的结果也不同
		print(num,'是一个质数')
#使用内置 enumerate 函数进行遍历:
sequence=[12,13,14,15,16]
for i,j in enumerate(sequence):
	print(i,j) #i是角标 j是具体数值
prime = []
for num in range(2,100): #迭代2到100之间的数字
	for i in range(2,num): #根据因子进行迭代
		if num%i == 0:	#确定最后因子
			break	#退出当前循环
	else:
		prime.append(num)
print (prime)
#dic字典也就是map映射 键值对的方式，
dic1={"wangkaijin":"good","age":10}
print(dic1['wangkaijin'],"---",dic1['age'])
dic2 = {'xiaoming':'niaho','age':20}
dic2['xiaoming']="xiaowang"
print(dic2['xiaoming'],"gg",dic2['age'])
#求绝对值abs(a),只有一个参数TypeError的错误，
#并且Python会明确地告诉你：abs()有且仅有1个参数，
#但给出了两个：
#max()为最大值
print("\n",abs(-3),"--",max(0,1,3,-1))
#数据类型转换
#int（）整型 bool()布尔型 float('a.3')浮点型str（）字符型
#函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，
#相当于给这个函数起了一个“别名”：
a=abs #变量a相当于只想abs函数对象
a(-1) #相当于调用了abs方法
print(a(-2))
# 如果没有return语句，函数执行完毕后也会返回结果，只是结果为None。#
