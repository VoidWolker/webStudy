#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

"""
Models of userInfo, blog, comment
"""

___author__ = "vw"

import time, uuid

from www.orm import Model, StringField, BooleanField, FloatFiled, TextField


def next_id():
    return "%015d%s000" % (int(time.time()) * 1000, uuid.uuid4().hex )


class UserInfo(Model):

    __table__ = "UserInfo"

    id = StringField(primary_key=True, default=next_id, ddl="varchar(50)")
    email = StringField(ddl="varchar(50)")
    passwd = StringField(ddl="varchar(50)")
    admin = BooleanField()
    name = StringField(ddl="varchar(50)")
    image = StringField(ddl="varchar(500)")
    created_at = FloatFiled(default=time.time)


class Blog(Model):

    __table__ = "blogs"

    id = StringField(primary_key=True, default=next_id, ddl="varchar(50)")
    user_id = StringField(ddl="varchar(50)")
    user_image = StringField(ddl="varchar(500)")
    name = StringField(ddl="varchar(50)")
    summary = StringField(ddl="varchar(200)")
    content = TextField()
    crated_at = FloatFiled(default=time.time)


class Comment(Model):

    __table__ = "comments"

    id = StringField(primary_key=True, default=next_id, ddl="varchar(50)")
    blog_id = StringField(ddl="varchar(50)")
    user_id = StringField(ddl="varchar(50)")
    user_name = StringField(ddl="varchar(50)")
    user_image = StringField(ddl="varchar(500)")
    content = TextField()
    created_at = FloatFiled(default=time.time)
