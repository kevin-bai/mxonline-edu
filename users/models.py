# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name=u"用户昵称")
    birth_day = models.DateField(verbose_name=u"生日", null=True, blank="" )
    gender = models.CharField(max_length=5, choices=(("mail", u"男"), ("femail", u"女")))
    address = models.CharField(max_length=128, null=True, blank="", verbose_name=u"地址", default="")
    phone = models.IntegerField(null=True, blank="", verbose_name=u"手机")
    avatar = models.ImageField(upload_to="image/%Y/%M", default=u"images/default.png", max_length=100, verbose_name=u"头像")

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    # 重载这个方法，否在在print UserProfile的实例的时候，不能打印我们自定义的字符串
    def __unicode__(self):
        return self.username
