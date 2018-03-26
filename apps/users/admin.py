# _*_ coding:utf-8 _*_
from django.contrib import admin

# Register your models here.

from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    pass


# 把admin和model进行关联注册
admin.site.register(UserProfile, UserProfileAdmin)
