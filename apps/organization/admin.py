# _*_ coding:utf-8 _*_
from django.contrib import admin

# Register your models here.

from .models import CourseOrg
from .models import Teacher


class CourseOrgAdmin(admin.ModelAdmin):
    pass


class TeacherAdmin(admin.ModelAdmin):
    pass


admin.site.register(CourseOrg, CourseOrgAdmin)
admin.site.register(Teacher, TeacherAdmin)
