# _*_ coding:utf-8 _*_

__author__ = 'kevin'
__date__ = '2018/3/28 12:36'

import xadmin

import models as course
from utils.obj2list import get_list_display, get_search_fields


class LessonInline(object):
    model = course.Lesson
    extra = 0


class CourseResourseInline(object):
    model = course.CourseResource
    extra = 0


class CourseAdmin(object):
    obj = course.Course
    list_display = ['name', 'id', 'course_org', 'teacher', 'desc', 'degree', 'click_num']
    search_fields = get_search_fields(obj)
    list_filter = get_list_display(obj)
    # 显示排序
    ordering = ['-click_num']
    # 只读字段
    readonly_fields = ['click_num']
    # 去除字段显示
    exclude = ['favourite_mun']
    # icon
    model_icon = 'fa fa-group'

    inlines = [LessonInline, CourseResourseInline]


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
