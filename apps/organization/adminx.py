# _*_ encoding:utf-8 _*_
import xadmin

import models as org
from utils.obj2list import get_list_display,get_search_fields


class CityDictAdmin(object):
    obj = org.CityDict
    list_display = get_list_display(obj)
    search_fields = get_search_fields(obj)
    list_filter = get_list_display(obj)


class CourseOrgAdmin(object):
    obj = org.CourseOrg
    list_display = get_list_display(obj)
    search_fields = get_search_fields(obj)
    list_filter = get_list_display(obj)
    # 当有个外键指向他的时候，以搜索模式
    relfield_style = 'fx-ajax'


class TeacherAdmin(object):
    obj = org.Teacher
    list_display = get_list_display(obj)
    search_fields = get_search_fields(obj)
    list_filter = get_list_display(obj)


xadmin.site.register(org.CourseOrg, CourseOrgAdmin)
xadmin.site.register(org.Teacher, TeacherAdmin)
xadmin.site.register(org.CityDict, CityDictAdmin)
