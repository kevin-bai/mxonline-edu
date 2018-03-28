# _*_ coding:utf-8 _*_

__author__ = 'kevin'
__date__ = '2018/3/28 12:32'

import xadmin

import models as operation
from utils.obj2list import get_list_display, get_search_fields


class UserAskAdmin(object):
    obj = operation.UserAsk
    list_display = get_list_display(obj)
    search_fields = get_search_fields(obj)
    list_filter = get_list_display(obj)


class CourseCommentsAdmin(object):
    obj = operation.CourseComments
    list_display = get_list_display(obj)
    search_fields = get_search_fields(obj)
    list_filter = get_list_display(obj)


class UserFavoriteAdmin(object):
    obj = operation.UserFavorite
    list_display = get_list_display(obj)
    search_fields = get_search_fields(obj)
    list_filter = get_list_display(obj)


class UserMessageAdmin(object):
    obj = operation.UserMessage
    list_display = get_list_display(obj)
    search_fields = get_search_fields(obj)
    list_filter = get_list_display(obj)


class UserCourseAdmin(object):
    obj = operation.UserCourse
    list_display = get_list_display(obj)
    search_fields = get_search_fields(obj)
    list_filter = get_list_display(obj)


xadmin.site.register(operation.UserAsk, UserAskAdmin)
xadmin.site.register(operation.CourseComments, CourseCommentsAdmin)
xadmin.site.register(operation.UserFavorite, UserFavoriteAdmin)
xadmin.site.register(operation.UserMessage, UserMessageAdmin)
xadmin.site.register(operation.UserCourse, UserCourseAdmin)
