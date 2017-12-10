#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from wsgiref.simple_server import make_server

def application(environ,start_response):
    start_response('200 OK',[('content-type','text/html')])
    body='<h1>nihao,%s</h1>'%(environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]
httpd = make_server('localhost',9000,application)
print('开始监听9000端口...')
httpd.serve_forever()