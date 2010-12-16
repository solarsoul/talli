#!/usr/bin/env python
#-*- coding: utf-8 -*-

import tornado.httpserver
import tornado.ioloop
import tornado.web
from mongokit import *

import os

import blog
from blog import models, views

conn = Connection()
models.register_models(conn)

settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "cookie_secret": "61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
    "login_url": "/login",
    "xsrf_cookies": True,
    'template_path': os.path.join(os.path.dirname(__file__), "templates"),
}

application = tornado.web.Application([
    (r"/", views.Index, dict(database=conn)),
    (r"/manager/", views.AdminIndex, dict(database=conn)),
], **settings)

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)

    print "Server started..."
    tornado.ioloop.IOLoop.instance().start()
