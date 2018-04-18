# _*_ coding:utf-8 _*_

__author__ = 'kevin'
__date__ = '2018/4/18 11:14'

from django.conf.urls import url, include

from .views import CourseListView,CourseDetailView,CourseCommentView,CourseVideoView

urlpatterns = [
    # 课程列表项
    url(r'^list/$', CourseListView.as_view(), name='course_list'),
    # 课程列表项
    url(r'^detail/$', CourseDetailView.as_view(), name='course_detail'),
    # 课程列表项
    url(r'^comment/$', CourseCommentView.as_view(), name='course_comment'),
    # 课程列表项
    url(r'^video/$', CourseVideoView.as_view(), name='course_video'),
]
