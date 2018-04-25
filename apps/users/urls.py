# _*_ coding:utf-8 _*_

__author__ = 'kevin'
__date__ = '2018/4/23 14:16'

from django.conf.urls import url, include

from .views import UserInfoView, UserCourseView, UserFavoriteOrgView, UserMessageView, UserImageUpload, UserModifyPwdView, \
    SendEmailCodeView,UserUpdateEmailView,UserFavoriteTeacherView,UserFavoriteCourseView

urlpatterns = [
    # 用户信息页面
    url(r'^info/$', UserInfoView.as_view(), name='user_info'),
    # 用户课程页面
    url(r'^course/$', UserCourseView.as_view(), name='user_course'),
    # 用户消息页面
    url(r'^message/$', UserMessageView.as_view(), name='user_message'),
    # 用户收藏的机构页面
    url(r'^fav/org/$', UserFavoriteOrgView.as_view(), name='user_fav_org'),
    # 用户收藏的讲师页面
    url(r'^fav/teacher/$', UserFavoriteTeacherView.as_view(), name='user_fav_teacher'),
    # 用户收藏的课程页面
    url(r'^fav/course/$', UserFavoriteCourseView.as_view(), name='user_fav_course'),
    # 用户头像上传
    url(r'^image/upload/$', UserImageUpload.as_view(), name='user_imageUpload'),
    # 用户个人中心修改密码
    url(r'^modify/pwd/$', UserModifyPwdView.as_view(), name='user_modifyPwd'),
    # 发送邮箱验证码
    url(r'^send_email_code/$', SendEmailCodeView.as_view(), name='user_send_email_code'),
    # 用户更改邮箱
    url(r'^update_email/$', UserUpdateEmailView.as_view(), name='user_update_email'),
]


