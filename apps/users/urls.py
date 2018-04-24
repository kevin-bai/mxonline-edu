# _*_ coding:utf-8 _*_

__author__ = 'kevin'
__date__ = '2018/4/23 14:16'

from django.conf.urls import url, include

from .views import UserInfoView, UserCourseView, UserFavoriteView, UserMessageView,UserImageUpload

urlpatterns = [
    # 用户信息页面
    url(r'^info/$', UserInfoView.as_view(), name='user_info'),
    # 用户课程页面
    url(r'^course/$', UserCourseView.as_view(), name='user_course'),
    # 用户消息页面
    url(r'^message/$', UserMessageView.as_view(), name='user_message'),
    # 用户收藏页面
    url(r'^fav/$', UserFavoriteView.as_view(), name='user_fav'),
    # 用户头像上传
    url(r'^image/upload/$',UserImageUpload.as_view(), name='user_imageUpload')
]
