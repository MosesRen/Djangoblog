# -*- coding: UTF-8 -*-
__author__ = 'mosesren'
__date__ = '2018/3/27 20:29'

import xadmin
from.models import *
class  Catagoryadmin(object):
    list_display = ['name']
class  Tagadmin(object):
    list_display = ['name']
class blogpost(object):
    filter_vertical = ('tags')
    list_display = ['title','catagory','tags','text','time']
class AboutAdmin(object):
    list_display = ['title','text','img']

xadmin.site.register(ArticleTag, Tagadmin)
xadmin.site.register(ArticleCatagory, Catagoryadmin)
xadmin.site.register(blogtext,blogpost)
xadmin.site.register(aboutme,AboutAdmin)
