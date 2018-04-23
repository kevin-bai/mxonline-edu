# _*_ coding:utf-8 _*_
from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
import json

from .models import CityDict, CourseOrg, Teacher
from .form import UserAskForm
from operation.models import UserFavorite


class OrglistView(View):
    """
    课程机构
    """

    def get(self, request):
        # 课程机构
        all_orgs = CourseOrg.objects.all()

        # 搜索功能
        search_word = request.GET.get('search', '')
        if search_word:
            all_orgs = CourseOrg.objects.filter(
                Q(name__icontains=search_word) | Q(desc__icontains=search_word))

        # 点击数降序 取前三个
        hot_orgs = all_orgs.order_by("-click_num")[:3]
        # 城市
        all_citys = CityDict.objects.all()
        # 根据城市筛选
        city_id = request.GET.get('city', '')
        if city_id:
            all_orgs = CourseOrg.objects.filter(city_id=int(city_id))

        # 类别筛选
        ct_id = request.GET.get('ct', '')
        if ct_id:
            all_orgs = all_orgs.filter(category=ct_id)

        # 排序
        sort = request.GET.get('sort', '')
        if sort:
            if sort == 'students':
                all_orgs = all_orgs.order_by('-students_num')
            elif sort == 'courses':
                all_orgs = all_orgs.order_by('-course_num')
        # 课程结构分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # Provide Paginator with the request object for complete querystring generation

        p = Paginator(all_orgs, 3, request=request)

        orgs_list = p.page(page)

        # return render_to_response('index.html', {
        #     'people': people,
        # }

        org_nums = all_orgs.count()
        return render(request, 'org-list.html', {
            'all_orgs': orgs_list,
            'all_citys': all_citys,
            'org_num': org_nums,
            'city_id': city_id,
            'ct_id': ct_id,
            'hot_orgs': hot_orgs
        })


class AddAskView(View):
    # 用户添加咨询
    def post(self, request):
        user_ask_form = UserAskForm(request.POST)
        if user_ask_form.is_valid():
            # name = request.POST.get('name', '')
            # mobile = request.POST.get('mobile', '')
            # course_name = request.POST.get('course_name', '')
            #
            # user_ask = UserAskForm()
            # user_ask.name = name
            # user_ask.mobile = mobile
            # user_ask.course_name = course_name
            # user_ask.save()

            user_ask = user_ask_form.save(commit=True)
            result = {'status': 'success'}
            return HttpResponse(json.dumps(result), content_type='application/json')
        else:
            result = {'status': 'fail', 'msg': user_ask_form.errors}
            return JsonResponse(result)


class OrgHomeView(View):
    """
    机构主页
    """

    def get(self, request, org_id):
        course_org = CourseOrg.objects.get(id=int(org_id))
        has_fav = False
        if request.user.is_authenticated:
            fav_record = UserFavorite.objects.filter(user=request.user, fav_id=int(org_id), fav_type=2)
            if fav_record:
                has_fav = True
        # 通过course的外键course_org，反向查找所有的course。有外键的地方都可以这样做
        all_course = course_org.course_set.all()[:3]
        all_teacher = course_org.teacher_set.all()[:3]
        return render(request, 'org-detail-homepage.html', {
            'org_id': org_id,
            'course_org': course_org,
            'all_course': all_course,
            'all_teacher': all_teacher,
            'has_fav': has_fav
        })


class OrgTeacherView(View):
    """
    机构讲师页
    """

    def get(self, request, org_id):
        course_org = CourseOrg.objects.get(id=int(org_id))
        has_fav = False
        if request.user.is_authenticated:
            fav_record = UserFavorite.objects.filter(user=request.user, fav_id=int(org_id), fav_type=2)
            if fav_record:
                has_fav = True
        all_teacher = course_org.teacher_set.all()[:3]
        return render(request, 'org-detail-teachers.html', {
            'org_id': org_id,
            'course_org': course_org,
            'all_teacher': all_teacher,
            'has_fav': has_fav
        })


class TeacherListView(View):
    def get(self, request):
        all_teacher = Teacher.objects.all()

        # 搜索功能
        search_word = request.GET.get('search', '')
        if search_word:
            all_teacher = Teacher.objects.filter(
                Q(name__icontains=search_word) | Q(work_company__icontains=search_word) | Q(
                    work_position__icontains=search_word) | Q(points__icontains=search_word)
                )

        sort = request.GET.get('sort', '')
        hot_teachers = all_teacher.order_by('-click_num')
        if sort == 'hot':
            teachers = hot_teachers
        else:
            teachers = all_teacher.order_by('-add_time')

        return render(request, 'teachers-list.html', {
            'teachers': teachers,
            'hot_teachers': hot_teachers
        })


class TeacherDetailView(View):
    """
    讲师详情
    """

    def get(self, request, teacher_id):
        teacher = Teacher.objects.get(id=teacher_id)
        if not teacher:
            return render(request, '404.html')
        hot_teachers = Teacher.objects.all().order_by('-click_num')[:3]
        all_courses = teacher.course_set.all()

        # 收藏
        fav_record_teacher = False
        fav_record_org = False
        if request.user.is_authenticated:
            fav_record_teacher = UserFavorite.objects.filter(user=request.user, fav_id=int(teacher_id), fav_type=3)
            if fav_record_teacher:
                fav_record_teacher = True
            fav_record_org = UserFavorite.objects.filter(user=request.user, fav_id=int(teacher.org.id),
                                                         fav_type=2)
            if fav_record_org:
                fav_record_org = True

        return render(request, 'teacher-detail.html', {
            'teacher': teacher,
            'all_courses': all_courses,
            'hot_teachers': hot_teachers,
            'has_fav_teacher': fav_record_teacher,
            'has_fav_org': fav_record_org
        })


class OrgDescView(View):
    """
    机构介绍页
    """

    def get(self, request, org_id):
        course_org = CourseOrg.objects.get(id=int(org_id))
        has_fav = False
        if request.user.is_authenticated:
            fav_record = UserFavorite.objects.filter(user=request.user, fav_id=int(org_id), fav_type=2)
            if fav_record:
                has_fav = True
        return render(request, 'org-detail-desc.html', {
            'org_id': org_id,
            'course_org': course_org,
            'has_fav': has_fav
        })


class OrgCourseView(View):
    """
    机构课程页
    """

    def get(self, request, org_id):
        course_org = CourseOrg.objects.get(id=int(org_id))
        has_fav = False
        if request.user.is_authenticated:
            fav_record = UserFavorite.objects.filter(user=request.user, fav_id=int(org_id), fav_type=2)
            if fav_record:
                has_fav = True
        all_course = course_org.course_set.all()[:3]
        return render(request, 'org-detail-course.html', {
            'org_id': org_id,
            'course_org': course_org,
            'all_course': all_course,
            'has_fav': has_fav
        })


class AddFavorView(View):
    """
    用户收藏，用户取消收藏
    """

    def post(self, request):
        fav_id = request.POST.get('fav_id', 0)
        fav_type = request.POST.get('fav_type', 0)

        # django 内置的user类，和我们定义的不一样
        # 判断用户登录状态
        if not request.user.is_authenticated():
            return JsonResponse({'status': 'failed', 'msg': u'用户未登录'})

        # 直接通过request找到user
        exist_record = UserFavorite.objects.filter(user=request.user, fav_id=int(fav_id), fav_type=int(fav_type))

        if exist_record:
            exist_record.delete()
            return JsonResponse({'status': 'success', 'fav_status': False})
        else:
            record = UserFavorite()
            if int(fav_id) > 0 and int(fav_type) > 0:
                record.user = request.user
                record.fav_id = int(fav_id)
                record.fav_type = int(fav_type)
                record.save()
                return JsonResponse({'status': 'success', 'fav_status': True})
            else:
                return JsonResponse({'status': 'success', 'fav_status': False})
