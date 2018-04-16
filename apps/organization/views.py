# _*_ coding:utf-8 _*_
from django.shortcuts import render
from django.views.generic.base import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from .models import CityDict, CourseOrg


class OrglistView(View):
    """
    课程机构
    """

    def get(self, request):
        # 课程机构
        all_orgs = CourseOrg.objects.all()

        # 城市
        all_citys = CityDict.objects.all()

        # 根据城市筛选
        city_id = request.GET.get('city', '')
        if city_id:
            all_orgs = CourseOrg.objects.filter(city_id=int(city_id))

        # 类别筛选
        ct_id = request.GET.get('ct', '')
        if ct_id:
            all_orgs = CourseOrg.objects.filter(category=ct_id)

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
            'ct_id': ct_id
        })
