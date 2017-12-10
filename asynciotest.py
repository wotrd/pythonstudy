#!/usr/cin/env python3
# -*- coding:utf-8 -*-
import asyncio
#导入线程
import threading
# @asyncio.coroutine
# def hello():
#     print('hello world! %s'% threading.current_thread())
#     #调用asyncio.sleep(1)
#     r = yield from asyncio.sleep(1)
#     print('hello again %s'% threading.current_thread())
#
# loop=asyncio.get_event_loop()
# #开始执行hello方法
# tasks=[hello(),hello()]
# #执行多个task函数
# loop.run_until_complete (asyncio.wait(tasks))
# #关闭loop
# loop.close()

@asyncio.coroutine
def wget(host):
    print('wegt %s...'%host)
    connect=asyncio.open_connection(host,80)
    reader ,writer = yield from connect
    header = 'GET/HTTP/1.0\r\nHost:%s\r\n\r\n'% host
    writer .write(header.encode('utf-8'))
    yield from writer.drain()   #刷新缓冲区
    while True:
        line = yield from reader.readline()
        if line==b'\r\n':
            break
        print('%s header > %s'%(host,line.decode('utf-8').rstrip()))
        #ignore the body ,close the socket
        writer.close()

loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.cn','www.sohu.com','www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

