# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime

from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name=u"用户昵称")
    birth_day = models.DateField(verbose_name=u"生日", null=True, blank=True)
    gender = models.CharField(max_length=6, choices=(("male", u"男"), ("female", u"女")), verbose_name=u'性别')
    address = models.CharField(max_length=128, null=True, blank=True, verbose_name=u"地址", default="")
    phone = models.CharField(max_length=11, null=True, blank=True, verbose_name=u"手机")
    avatar = models.ImageField(upload_to="image/%Y/%m", default=u"images/default.png", max_length=100,
                               verbose_name=u"头像")

    # from operation.models import UserMessage

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    # 重载这个方法，否在在print UserProfile的实例的时候，不能打印我们自定义的字符串
    def __unicode__(self):
        return self.username

    def get_unread_nums(self):
        # 获取未读消息的数量
        # 这个import不能放在头部，因为会造成循环 引用
        from operation.models import UserMessage
        messages = UserMessage.objects.filter(user=self.id,has_read=False)
        return messages.count()


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name=u"验证码")
    email = models.EmailField(max_length=50, verbose_name=u"邮箱")
    send_type = models.CharField(max_length=20, choices=(('register', u"注册"), ('forget', u"忘记密码"), ('update', u'修改邮箱')),
                                 verbose_name=u"验证类型")
    # default=datetime.now() 后面括号一定要去掉，不然取得是进入这行代码的时间，括号去掉才是这个class实例化的时间
    send_time = models.DateField(default=datetime.now, verbose_name=u"发送时间")

    class Meta:
        verbose_name = u"邮箱验证码"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return '{0}({1})'.format(self.code, self.email)


class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name=u"标题")
    image = models.ImageField(max_length=100, upload_to="banner/%Y/%m", verbose_name=u"轮播图")
    url = models.CharField(max_length=200, verbose_name=u"访问地址")
    index = models.IntegerField(verbose_name=u"顺序", default=100)
    add_time = models.DateField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"轮播图"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title
