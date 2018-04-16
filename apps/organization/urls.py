# _*_ coding:utf-8 _*_

__author__ = 'kevin'
__date__ = '2018/4/16 17:28'

from django.conf.urls import url, include

from .views import OrglistView

urlpatterns = [
    # 课程机构列表项
    url(r'^list/$', OrglistView.as_view(), name='org_list'),

]
