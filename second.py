#!/usr/bin/env python3
# -*- codign: utf-8 -*-
print("nihao")

#ord()函数用来获取字母对应的数字
ord('W')
#char()

#str通过encode()方法可以编码为指定的bytes
name = input('你好，请输入')

print('name='+name)

print(name.encode("utf-8"))
b=name.encode("utf-8")
print(b.decode('utf-8'))
#print(name.encode("ascii"))
#格式化字符
#%运算符就是用来格式化字符串的。在字符串内部，%s表示用字符串替换，%d表示用整数替换，
#有几个%?占位符，后面就跟几个变量或者值，顺序要对应好。如果只有一个%?，括号可以省略。
name1 = '%d-%02d' % (3,2) 	#%2d为空格，%02d为补零
print (name1)
name2 = 'hello,%s . %s' %(name,True)
print (name2)
#list列表类似于数组，不过可以存放不同类型的数据
list1 = ['niaho','python','gg']
print (list1)
list1.append('ok')
print (list1)
list1.pop()
print (list1)
list1.pop(1)
print (list1)
list1.insert(3,'insert')
print (list1)
list1[1]='god'
print (list1)
print('length=',len(list1))
#tuple 元组 但是tuple一旦初始化就不能修改,而且没有insert等方法
a=(1,2,'niaho')
print (a)
b=('h')
print (b)
#有1个元素的tuple定义时必须加一个逗号,，
c=(1,)
print (c)
#tuple不可变，但要需要改变可以使用list嵌套
exit()