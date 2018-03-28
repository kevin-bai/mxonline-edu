# _*_ coding:utf-8 _*_

__author__ = 'kevin'
__date__ = '2018/3/27 19:41'

import xadmin
from xadmin import views

from .models import EmailVerifyRecord
from .models import Banner


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class CommonSetting(object):
    site_title = u'慕学在线后台管理'
    site_footer = u'慕学在线'
    menu_style = 'accordion'  # 让menu可以收缩


class EmailVerifyRecordAdmin(object):
    # 列显示
    list_display = ['code', 'email', 'send_type', 'send_time']
    # 搜索显示
    search_fields = ['code', 'email', 'send_type']
    # 筛选字段
    list_filter = ['code', 'email', 'send_type', 'send_time']


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, CommonSetting)
