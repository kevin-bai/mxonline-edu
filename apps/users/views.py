# _*_ coding:utf-8 _*_
from django.shortcuts import render
from django.contrib.auth import authenticate, login


# Create your views here.


def login(request):
    if request.method == 'POST':
        user_name = request.POST.get('username', "")
        pass_word = request.POST.get('password', "")
        # 向数据库发起验证，用户名和密码是否正确
        user = authenticate(user_name, pass_word)
        if user is not None:
            # 调用django的login方法
            login(request, user)
            return render(request, 'index.html', {})
        else:
            print '登录失败'

    elif request.method == 'GET':
        return render(request, 'login.html', {})


def register(request):
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        return render(request, 'register.html', {})
