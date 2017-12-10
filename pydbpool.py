#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import asyncio
import logging;logging.basicConfig(level=logging.INFO)
import aiomysql

@asyncio.coroutine
def create_pool(loop,**kwargs):
    logging.info('create database pool connection ...')
    global __pool
    __pool = yield from aiomysql.create_pool(
        host=kwargs.get('host','localhost'),
        port = kwargs.get('port',3306),
        user = kwargs['user'],
        password=kwargs['password'],
        db = kwargs['db'],
        charset=kwargs.get('charset','utf-8'),
        autocommit=kwargs.get('autocommit',True),
        maxsize=kwargs.get('maxsize',10),
        minsize=kwargs.get('minsize',1),
        loop=loop
    )
@asyncio.coroutine
def select(sql,args,size=None):
    logging.info(sql+args)
    global __pool
    with (yield from __pool) as conn:
        cursor = yield from conn.cursor(aiomysql.DictCursor)
        yield from cursor.exexute(sql.replace('?','%s') , args or ())
        if size:
            values = yield from cursor.fetchmany(size)
        else :
            values = yield from cursor.fetchall()
        logging.info('rows returned %s'%len(values))
        yield from cursor.close()
        return values
@asyncio.coroutine
def exexute(sql,args):
    with (yield from __pool) as conn:
        try:
            cursor = yield from conn.cursor()
            yield from cursor.execute(sql.replace('?', '%s'), args)
            affected =cursor.rowcount
            yield from cursor.close()
        except BaseException as e:
            raise
        return affected
