#!/usr/bin/env python
# -*- coding: utf-8 -*-
#调试模式是否开启

DEBUG = True
SQLALCHEMY_TRACK_MODIFICATIONS = False
#session必须要设置key
SECRET_KEY='A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

#mysql数据库连接信息,这里改为自己的账号
SQLALCHEMY_DATABASE_URI = "mysql://root:root@127.0.0.1:3306/webpython"