#!/usr/bin/env python3
#-*- coding:utf-8 -*-
import mysql.connector
conn =mysql.connector.connect(user='root',port='3306',password='123456',database='fitnesslive.db')
cursor=conn.cursor()
cursor.execute('select * from user')
values = cursor.fetchall()
cursor .execute('drop table if EXISTS hello')

print(values[0])
conn.commit()
cursor.close()
conn.close()
#MySQL的SQL占位符是%s。
#除了select其他操作需要commit























# #导入mysql驱动
# import mysql.connector
# #注意把password设为你的root口令
# conn = mysql.connection.connect(user='root',password='password',database='test')
# cursor=conn.cursor()
# #创建user表
# cursor.execute('create table user(id varchar(20) primary KEY ,name varchar(20))')
# #插入一条记录，注意mysql的占位符是%s：
# cursor.execute('insert into user (id,name) values(%s,%s)',['1','mike'])
# cursor.rowcount
# #提交事务
# conn.commit()
# cursor.close()
# #运行查询
# cursor.cursor()
# cursor.execute('select * from user where id=%s',('1',))
# values=cursor.fetchall()
# values
# cursor.close()
# conn.close()
