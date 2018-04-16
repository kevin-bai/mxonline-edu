# _*_ coding:utf-8 _*_
from django.shortcuts import render
from django.views.generic.base import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from .models import CityDict, CourseOrg
from .form import UserAskForm


class OrglistView(View):
    """
    课程机构
    """

    def get(self, request):
        # 课程机构
        all_orgs = CourseOrg.objects.all()
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

    def post(self, request):
        user_ask_form = UserAskForm(request.POST)
        if user_ask_form.is_valid():
            name = request.POST.get('name', '')
            mobile = request.POST.get('mobile', '')
            course_name = request.POST.get('course_name', '')

            user_ask = UserAskForm()
            user_ask.name = name
            user_ask.mobile = mobile
            user_ask.course_name = course_name
            user_ask.save()

            return render(request, 'send_sucess.html', {'msg': u'提交成功'})
