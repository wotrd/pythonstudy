#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import logging;logging.basicConfig(level=logging.INFO)
import asynciotest,os,json,time
from aiohttp import web
import aiomysql
def index(request):
    return web.Response(body=b'<h1>Awesome</h1>',content_type='text/html')
@asynciotest.coroutine
def init(loop):
    app=web.Application(loop=loop)
    app.router.add_route('GET','/',index)
    srv=yield from loop.create_server(app.make_handler(),'127.0.0.1',8000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv
loop = asynciotest.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()

@asynciotest.coroutine
def create_pool(loop,**kw):
    logging.info('create database connection pool...')
    global __pool
    __pool = yield from aiomysql.connect(
        host = kw.get('host','localhost'),
        port = kw.get('port',3306),
        user = kw['user'],
        password = kw['password'],
        db=kw['db'],
        charset=kw.get('charset','utf-8'),
        autocommit = kw.get('autocommit',True),
        maxsize=kw.get('maxsize',10),
        minsize=kw.get('minsize',1),
        loop=loop
    )
@asynciotest.coroutine
def select(sql,args,size=None):
    logging.info(sql,args)
    global __pool
    with (yield from __pool) as conn:
        cur = yield from conn.cursor(aiomysql.DictCursor)#aiomysql.DictCursor可以通过字典获取数据
        yield from cur.execute(sql.replace('?','%s'),args or ())
        if size:
            rs=yield from cur.fetchmany(size)
        else:
            rs=yield from cur.fetchall()
    yield from cur.close()
    logging.info('rows returned: %s' % len(rs))
    return rs
@asynciotest.coroutine
def execute(sql,args):
    logging.info(sql,args)
    with(yield from __pool) as conn:
        try:
            cur=yield  from conn.cursor()
            yield from cur.execute(sql.replace('?','%s') % args)
            affected=cur.rowcount
            yield from cur.close()
        except BaseException as e:
            raise
        return affected
#ORM定义一个User对象，将数据库表users和 它关联起来

from orm import ModelField,StringField,IntegerField
class User(Model):      #类中的属性对应于数据库中的表，实例中的属性通过__init__方法进行初始化，两者互不干扰
    __table__ ='users'
    id =IntegerField(primary_key=True)
#创建实例
users = User(id=123,name='Machael')
#存入数据库
users.insert()
#查询所有数据库对象
users.findAll()
#定义左右orm映射的对象model
class Model(dict,metaclass=ModelMetaclass):
    def __init__(self,**kw):
        super(Model,self).__init__(**kw)
    def __gertattr__(self,key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)
    def __setattr__(self,key,value):
        self[key]=value
    def getValue(self,key):
        return getattr(self,key,None)
    def getValueOrDefault(self,key):
        value=getattr(self,key,None)
        if value is None:
            field =self.__mapping__[key]
            if field .default is not None:
                value=field.default() if callable(field.default) else field.default
                logging.debug('using defualt value for %s:%s' % (key,str(value)))
                setattr(self,key,value)
        return value
#model从dict中继承 ，所有dict的功能，同时具有了__getter__ 和 __setattr__,因此可以向引用普通字段那样使用


















