'''
Created on 2012-10-15

@author: Administrator
'''
from django.conf.urls import *

urlpatterns = patterns(('mybloga.views'),url(r'^bloglist/$','blog_list',name='bloglist'),)