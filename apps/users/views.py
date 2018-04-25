# _*_ coding:utf-8 _*_
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.hashers import make_password
from django.core.urlresolvers import reverse
import json

from .models import UserProfile, EmailVerifyRecord, Banner
from operation.models import UserCourse, UserMessage, UserFavorite
from .form import LoginForm, RegisterForm, ForgetForm, ResetForm, UploadImageForm, UserInfoForm
from organization.models import CourseOrg, Teacher
from courses.models import Course
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
        banners = Banner.objects.all()
        all_courses = Course.objects.all()[:6]
        all_orgs = CourseOrg.objects.all()
        all_courses_banner = Course.objects.all()[6:8]
        return render(request, 'index.html', {
            'banners':banners,
            'all_courses':all_courses,
            'all_orgs':all_orgs,
            'all_courses_banner':all_courses_banner
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
                    return HttpResponseRedirect(reverse('index'))
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

            # 写入欢迎注册消息
            user_message = UserMessage()
            user_message.user = user_profile.id
            user_message.message = u'欢迎注册慕学在线'
            user_message.save()

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
    """
    邮箱找回，修改密码
    """

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
        # reverse 可以根据 name直接反解成url地址
        return HttpResponseRedirect(reverse("index"))


class UserInfoView(LoginRequiredMixin, View):
    """
    用户中心页面
    """

    def get(self, request):
        return render(request, 'usercenter-info.html')

    def post(self, request):
        user_info_form = UserInfoForm(request.POST, instance=request.user)
        if user_info_form.is_valid():
            user_info_form.save()
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse(user_info_form.errors)


class UserCourseView(LoginRequiredMixin, View):
    """
    用户课程页面
    """

    def get(self, request):
        user_courses = UserCourse.objects.filter(user=request.user)
        all_courses = [user_course.course for user_course in user_courses]
        return render(request, 'usercenter-mycourse.html', {
            'all_courses': all_courses
        })


class UserMessageView(LoginRequiredMixin, View):
    """
    个人消息页面
    """

    def get(self, request):
        user_messages = UserMessage.objects.filter(user=request.user.id).order_by('-send_time')
        for user_message in user_messages:
            user_message.has_read = True
            user_message.save()
        # all_messages = [user_message for user_message in user_messages]
        return render(request, 'usercenter-message.html', {
            'all_messages': user_messages
        })


class UserFavoriteOrgView(LoginRequiredMixin, View):
    """
    用户收藏机构页面
    """

    def get(self, request):
        user_fav_orgs = UserFavorite.objects.filter(user=request.user, fav_type=2)
        fav_orgs = []
        for user_fav_org in user_fav_orgs:
            fav_org = CourseOrg.objects.get(id=user_fav_org.fav_id)
            fav_orgs.append(fav_org)

        return render(request, 'usercenter-fav-org.html', {
            'fav_orgs': fav_orgs
        })


class UserFavoriteTeacherView(LoginRequiredMixin, View):
    """
    用户收藏教师页面
    """

    def get(self, request):
        fav_objs = getFavObjs(request, fav_type=3)

        return render(request, 'usercenter-fav-teacher.html', {
            'fav_teachers': fav_objs
        })


class UserFavoriteCourseView(LoginRequiredMixin, View):
    """
    用户收藏课程页面
    """

    def get(self, request):
        fav_objs = getFavObjs(request, fav_type=1)

        return render(request, 'usercenter-fav-course.html', {
            'fav_courses': fav_objs
        })


def getFavObjs(request, fav_type=1):
    user_favs = UserFavorite.objects.filter(user=request.user, fav_type=fav_type)
    fav_objs = []
    if fav_type == 1:
        for user_fav in user_favs:
            fav_obj = Course.objects.get(id=user_fav.fav_id)
            fav_objs.append(fav_obj)
    if fav_type == 3:
        for user_fav in user_favs:
            fav_obj = Teacher.objects.get(id=user_fav.fav_id)
            fav_objs.append(fav_obj)
    return fav_objs


class UserImageUpload(LoginRequiredMixin, View):
    """
    修改用户头像
    """

    def post(self, request):
        # 文件类型和别的form字段不一样，不放在POST里面，放在request.FILES

        # image_form = UploadImageForm(request.POST, request.FILES)
        # if image_form.is_valid():
        #     image = image_form.cleaned_data['avatar']
        #     request.user.avatar = image
        #     request.user.save()

        # 简写：
        image_form = UploadImageForm(request.POST, request.FILES, instance=request.user)
        if image_form.is_valid():
            request.user.save()
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'fail'})


class UserModifyPwdView(View):
    """
    个人中心修改密码
    """

    def post(self, request):
        reset_form = ResetForm(request.POST)
        if reset_form.is_valid():
            pass_word1 = request.POST.get('password', '')
            pass_word2 = request.POST.get('password2', '')
            if pass_word1 != pass_word2:
                return JsonResponse({'status': 'fail', 'msg': '密码不一致'})
            user = request.user
            user.password = make_password(pass_word1)
            user.save()
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse(reset_form.errors)


class SendEmailCodeView(LoginRequiredMixin, View):
    """
    发送邮箱验证码
    """

    def get(self, request):
        email = request.GET.get('email', '')
        if UserProfile.objects.filter(email=email):
            return JsonResponse({'status': 'fail', 'email': u'邮箱已存在'})
        send_register_mail(email, 'update_email')
        return JsonResponse({'status': 'success', 'msg': u'邮箱验证码已发送'})


class UserUpdateEmailView(View):
    """
    用户更改密码
    """

    def post(self, request):
        email = request.POST.get('email', '')
        code_input = request.POST.get('code', '')
        verify_record = EmailVerifyRecord.objects.filter(email=email, code=code_input)
        if verify_record:
            request.user.email = email
            request.user.save()
            return JsonResponse({'status': 'success', 'msg': u'邮箱修改成功'})
        else:
            return JsonResponse({'status': 'fail', 'email': u'失败'})
