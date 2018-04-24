# _*_ coding:utf-8 _*_
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.hashers import make_password
from django.core.urlresolvers import reverse

from .models import UserProfile, EmailVerifyRecord
from .form import LoginForm, RegisterForm, ForgetForm, ResetForm,UploadImageForm
from utils.email_send import send_register_mail
from utils.mixin_utils import LoginRequiredMixin


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


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html', {

        })


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
                if user.is_active:
                    login(request, user)
                    return render(request, 'index.html', {'user_name': user_name, 'user': user})
                else:
                    return render(request, 'login.html', {'msg': u'用户名未激活'})
            else:
                return render(request, 'login.html', {'msg': u'用户名密码错误'})
        else:
            return render(request, 'login.html', {'login_form': login_form})


class RegisterView(View):

    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'register.html', {'register_form': register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            email = request.POST.get('email', '')
            if UserProfile.objects.filter(username=email):
                return render(request, 'register.html', {'msg': u"用户已存在", 'register_form': register_form})
            pass_word = request.POST.get('password', '')
            user_profile = UserProfile()
            user_profile.is_active = False
            user_profile.username = email
            user_profile.email = email
            user_profile.password = make_password(pass_word)
            user_profile.save()

            send_register_mail(email, 'register')
            return render(request, 'send_sucess.html', {'msg': u'邮件已经发送，请查收'})
        else:
            return render(request, 'register.html', {'register_form': register_form})


class ActiveUserView(View):
    def get(self, request, active_code):
        print 'ActiveUserView'
        all_code = EmailVerifyRecord.objects.filter(code=active_code)
        if all_code:
            for code in all_code:
                email = code.email
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()
                return render(request, 'login.html')
        else:
            return render(request, 'active_fail.html')


class ForgetPwdView(View):
    """
    忘记密码
    """

    def get(self, request):
        forget_form = ForgetForm()
        return render(request, 'forgetpwd.html', {'forget_form': forget_form})

    def post(self, request):
        forget_form = ForgetForm(request.POST)
        if forget_form.is_valid():
            email = request.POST.get('email')
            if UserProfile.objects.filter(email=email):
                send_register_mail(email, 'forget')
                return render(request, 'send_sucess.html')
            else:
                return render(request, 'forgetpwd.html', {'msg': u'用户不存在', 'forget_form': forget_form})
        else:
            return render(request, 'forgetpwd.html', {'forget_form': forget_form})


class ResetPasswordView(View):
    def get(self, request, reset_code):
        all_code = EmailVerifyRecord.objects.filter(code=reset_code)
        if all_code:
            for code in all_code:
                email = code.email
                _email = UserProfile.objects.get(email=email)
                return render(request, 'password_reset.html', {'email': _email})


class ModifyPwdView(View):
    def post(self, request):
        reset_form = ResetForm(request.POST)
        if reset_form.is_valid():
            email = request.POST.get('email')
            pass_word1 = request.POST.get('password', '')
            pass_word2 = request.POST.get('password2', '')
            if pass_word1 != pass_word2:
                return render(request, 'password_reset.html', {'msg': u'密码不一致'})
            user = UserProfile.objects.get(email=email)
            user.password = make_password(pass_word1)
            user.save()
            return render(request, 'chang_success.html')
        else:
            return render(request, 'password_reset.html', {'msg': u'错误'})


class LogoutView(View):
    """
    用户登出
    """

    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse("index"))


class UserInfoView(LoginRequiredMixin, View):
    """
    用户中心页面
    """

    def get(self, request):
        return render(request, 'usercenter-info.html')

    def post(self, request):
        pass


class UserCourseView(LoginRequiredMixin, View):
    """
    用户课程页面
    """

    def get(self, request):
        return render(request, 'usercenter-mycourse.html')


class UserMessageView(LoginRequiredMixin, View):
    """
    用户消息页面
    """

    def get(self, request):
        return render(request, 'usercenter-message.html')


class UserFavoriteView(LoginRequiredMixin, View):
    """
    用户收藏页面
    """

    def get(self, request):
        return render(request, 'usercenter-fav-org.html')


class UserImageUpload(LoginRequiredMixin, View):
    """
    修改用户头像
    """
    def post(self, request):
        # 文件类型和别的form字段不一样，不放在POST里面，放在request.FILES
        image_form = UploadImageForm(request.POST, request.FILES)
        if image_form.is_valid():
            image = image_form.cleaned_data['avatar']
            request.user.avatar = image
            request.user.save()

