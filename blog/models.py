#!/usr/bin/env python
#-*- coding: utf-8 -*-

import datetime

from mongokit import *

class User(Document):
    __collection__ = 'blog_users'
    __database__ = 'blog'
    structure = {
        'email': unicode,
        'name': unicode,
        'active': bool,
        'staff': bool,
        'superuser': bool,
        'password': unicode,
        'date_join': datetime.datetime,
        'last_in': datetime.datetime,
    }
    i18n = ['name']
    required_fields = [
        'active',
        'staff',
        'superuser',
        'date_join',
        'last_in',
    ]
    default_values = {
        'active': True,
        'staff': True,
        'superuser': True,
        'date_join': datetime.datetime.utcnow,
        'last_in': datetime.datetime.utcnow,
    }
    use_dot_notation = True

class BlogPost(Document):
    __collection__ = 'blog_posts'
    __database__ = 'blog'
    structure = {
        'title': unicode,
        'body': unicode,
        'author': User,
        'tags': [unicode],
        'rank': float,
        'date_creation': datetime.datetime,
    }
    i18n = ['title']
    required_fields = [
        'title',
        'author',
        'date_creation',
    ]
    default_values = {
        'rank': 0.0,
        'date_creation': datetime.datetime.utcnow,
    }
    use_dot_notation = True


def register_models(db):
    #conn = Connection()
    db.register([User, BlogPost, ])
    #conn..BlogPost()
