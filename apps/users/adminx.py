# _*_ coding:utf-8 _*_

__author__ = 'kevin'
__date__ = '2018/3/27 19:41'

import xadmin
from xadmin import views

from .models import EmailVerifyRecord


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class EmailVerifyRecordAdmin(object):
    # 列显示
    list_display = ['code', 'email', 'send_type', 'send_time']
    # 搜索显示
    search_fields = ['code', 'email', 'send_type']
    # 筛选字段
    list_filter = ['code', 'email', 'send_type', 'send_time']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
