# _*_ coding:utf-8 _*_

__author__ = 'kevin'
__date__ = '2018/4/16 17:28'

from django.conf.urls import url, include

from .views import OrglistView, AddAskView, OrgHomeView, OrgTeacherView, OrgCourseView, OrgDescView, AddFavorView, \
    TeacherListView, TeacherDetailView

urlpatterns = [
    # 课程机构列表项
    url(r'^list/$', OrglistView.as_view(), name='org_list'),
    # 咨询表单
    url(r'add_ask/$', AddAskView.as_view(), name='add_ask'),
    # 机构首页
    url(r'home/(?P<org_id>\d+)/$', OrgHomeView.as_view(), name='org_home'),
    # 机构教师
    url(r'teacher/(?P<org_id>\d+)/$', OrgTeacherView.as_view(), name='org_teacher'),
    # 机构课程
    url(r'course/(?P<org_id>\d+)/$', OrgCourseView.as_view(), name='org_course'),
    # 机构描述
    url(r'desc/(?P<org_id>\d+)/$', OrgDescView.as_view(), name='org_desc'),
    # 讲师列表页
    url(r'teacher/list/$', TeacherListView.as_view(), name='teacher_list'),
    # 讲师详情页
    url(r'teacher/detail/(?P<teacher_id>\d+)/$', TeacherDetailView.as_view(), name='teacher_detail'),
    # 添加收藏
    url(r'add_favor/$', AddFavorView.as_view(), name='add_favor'),
]
