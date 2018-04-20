# _*_ coding:utf-8 _*_

__author__ = 'kevin'
__date__ = '2018/4/18 11:14'

from django.conf.urls import url, include

from .views import CourseListView, CourseDetailView, CourseCommentView, CourseVideoView, AddComment

urlpatterns = [
    # 课程列表项
    url(r'^list/$', CourseListView.as_view(), name='course_list'),
    # 课程详情项
    url(r'^detail/(?P<course_id>\d+)$', CourseDetailView.as_view(), name='course_detail'),
    # 课程评论项
    url(r'^comment/(?P<course_id>\d+)$', CourseCommentView.as_view(), name='course_comment'),
    # 课程章节项
    url(r'^video/(?P<course_id>\d+)$', CourseVideoView.as_view(), name='course_video'),

    url(r'^add_comment/$', AddComment.as_view(), name='add_comment'),
]
