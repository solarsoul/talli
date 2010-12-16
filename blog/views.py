#!/usr/bin/env python
#-*- coding: utf-8 -*-

import tornado.web

import models

class BlogHandler(tornado.web.RequestHandler):
    def initialize(self, database):
        self.database = database.blog


class Index(BlogHandler):
    def get(self):
        #new_post = self.database.blog.i18n.BlogPost()
        #new_post['title'] = 'test'
        #print new_post.save()
        #self.write("Hello, world")
        print self.database.BlogPost.find()
        self.render("index.html", title="My title", posts=self.database.BlogPost.find())

class AdminIndex(BlogHandler):
    def get(self):
        self.render("admin/index.html",
            title="My title",
            posts=self.database.BlogPost.find()
        )

if __name__ == "__main__":
    from mongokit import *
    conn = Connection()
    models.register_models(conn) 
    new_post = conn.blog.BlogPost()
    print new_post
    new_post.title= u'sss'
    new_post.author = u'Me'
    #new_post.save()
    cur = conn.blog.BlogPost.find()
    for p in cur:
        print p
    #new_post.save()
