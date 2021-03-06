# _*_ encoding:utf-8 _*_
"""mxonline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
import xadmin
from django.views.static import serve

from django.views.generic import TemplateView

from users.views import LoginView, RegisterView, ActiveUserView, ForgetPwdView, \
    ResetPasswordView, ModifyPwdView, LogoutView, IndexView
from organization.views import OrglistView
from mxonline.settings import MEDIA_ROOT
from DjangoUeditor.urls import get_ueditor_controller

urlpatterns = [
    url(r'^captcha/', include('captcha.urls')),
    # url(r'^ueditor/', include('DjangoUeditor.urls')),
    url(r'^ueditor/', get_ueditor_controller),
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^forgetpwd/$', ForgetPwdView.as_view(), name='forgetpwd'),
    url(r'^active/(?P<active_code>.*)/$', ActiveUserView.as_view()),
    url(r'^resetPwd/(?P<reset_code>.*)/$', ResetPasswordView.as_view(), name='reset_pwd'),
    url(r'^modify_pwd/$', ModifyPwdView.as_view(), name='modify_pwd'),
    # 课程机构url配置
    url(r'^org/', include('organization.urls', namespace='org')),
    # 课程url配置
    url(r'^course/', include('courses.urls', namespace='course')),
    # 课程url配置
    url(r'^user/', include('users.urls', namespace='user')),
    # 处理media图片的路径
    url(r'^media/(?P<path>.*)/$', serve, {'document_root': MEDIA_ROOT}),
    # 处理static图片的路径
    # url(r'^static/(?P<path>.*)/$', serve, {'document_root': STATIC_ROOT})
]

# 全局404页面配置
handler404 = 'users.views.page_not_found'
# 全局500页面配置
handler500 = 'users.views.page_error'
