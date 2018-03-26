# _*_ coding:utf-8 _*_
from django.contrib import admin

# Register your models here.

from .models import Course


class CourseAdmin(admin.ModelAdmin):
    pass


admin.site.register(Course, CourseAdmin)
