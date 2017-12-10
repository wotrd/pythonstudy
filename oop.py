#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__='wkj'


#起作用的：
class Fruits(object):
	# __slots__=('name','score')
	__slots__=('name','score')
	def __init__(self,name):
		self.name=name	
	
fruit=Fruits('xioawang')
fruit.name='xiaozhang'
fruit.score=23
print(fruit.score)

class Student(object):
	@property
	def birth(self):
		return self._birth

	@birth.setter
	def birth(self,value):
		self._birth=value
	@property
	def age(self):
		return 2015-self._birth
class Student(object):	#object表示父类
	def __init__(self,name,score):#初始化类似于构造函数
		self.name=name
		self.score=score
		#self.__name=name 表示name为私有的
	def __len__(self):
		return 100
	def print_score(self):
		print("%s:%s" % (self.name,self.score))
bart = Student("bart",59)
lisa = Student("lisa",23)
bart.print_score()
lisa.print_score()
bart.__len__
#__name__ 代表私有属性 _name表示不建议呗访问的
#前后都有双想划线的为特殊变量可以被直接使用
#判断一个变量是否是某个类型可以用isinstance()判断：
print(isinstance(bart,Student))
print(isinstance(1,str))
#这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，
#走起路来像鸭子”，那它就可以被看做是鸭子。
#判断队形类型，使用type()
#以使用isinstance()函数。判断属于某个实例

print(type(124))
print(type('str'))
print(type(bart))
# 使用dir()函数，它返回一个
# 包含字符串的list，比如，获得一个str对象的所有属性和方法
print(dir(bart))
#自己写的类，如果也
#想用len(myObj)的话，就自己写一个__len__()方法：

# ，如果我们想要限制实例的属性怎么办？比如，只允许对Student
# 实例添加name和age属性。为了达到限制的目的，Python允许在定
# 义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：
# ，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不