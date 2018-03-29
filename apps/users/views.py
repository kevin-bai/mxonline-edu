# _*_ coding:utf-8 _*_
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View

from .models import UserProfile
from .form import LoginForm

# Create your views here.


class CustomBackend(ModelBackend):
    # 这里重写authenticate函数，下面user_login中就会调用这里重写的函数
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            # 通过Q 实现查找的or操作， 用户可以用username 或者email登录
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            # 通过user继承的AbstractUser中的方法
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class LoginView(View):

    def get(self, request):
        return render(request, 'login.html', {})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get('username', "")
            pass_word = request.POST.get('password', "")
            # 向数据库发起验证，用户名和密码是否正确
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                # 调用django的login方法
                login(request, user)
                return render(request, 'index.html', {'user_name': user_name, 'user': user})
            else:
                return render(request, 'login.html', {'msg': u'用户名密码错误'})
        else:
            return render(request, 'login.html', {'login_form': login_form})