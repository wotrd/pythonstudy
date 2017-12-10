#@/usr/bin/env python3
# -*- coding:utf-8 -*-

'a simple model test'
__author__='wkj'
import sys

def test():
	args=sys.argv
	if len(args)==1:
		print("hello python")
	elif len(args)==2:
			print("hello %s" % args[1])
	else:
		print("too much arguments!")

if __name__=='__main__':
	print('gg'+test.__name__)
	test()
#要添加自己的搜索目录，有两种方法：
#sys.path.append('/Users/michael/my_py_scripts')
