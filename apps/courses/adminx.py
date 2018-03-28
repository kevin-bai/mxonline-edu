# _*_ coding:utf-8 _*_

__author__ = 'kevin'
__date__ = '2018/3/28 12:36'

import xadmin

import models as course
from utils.obj2list import get_list_display, get_search_fields


class CourseAdmin(object):
    obj = course.Course
    list_display = get_list_display(obj)
    search_fields = get_search_fields(obj)
    list_filter = get_list_display(obj)


class LessonAdmin(object):
    obj = course.Lesson
    list_display = get_list_display(obj)
    search_fields = get_search_fields(obj)
    list_filter = get_list_display(obj)


class VideoAdmin(object):
    obj = course.Video
    list_display = get_list_display(obj)
    search_fields = get_search_fields(obj)
    list_filter = get_list_display(obj)


class CourseResourceAdmin(object):
    obj = course.CourseResource
    list_display = get_list_display(obj)
    search_fields = get_search_fields(obj)
    list_filter = get_list_display(obj)


xadmin.site.register(course.Course, CourseAdmin)
xadmin.site.register(course.Lesson, LessonAdmin)
xadmin.site.register(course.Video, VideoAdmin)
xadmin.site.register(course.CourseResource, CourseResourceAdmin)
