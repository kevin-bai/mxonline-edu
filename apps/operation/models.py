# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime

from django.db import models

from courses.models import Course
from users.models import UserProfile


# Create your models here.


class UserAsk(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'姓名')
    mobile = models.CharField(max_length=11, null=True, blank="", verbose_name=u"电话")
    course_name = models.CharField(max_length=50, verbose_name=u'课程名')
    add_time = models.DateField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'用户咨询'
        verbose_name_plural = verbose_name


class CourseComments(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u'用户')
    course = models.ForeignKey(Course, verbose_name=u'课程')
    comment = models.CharField(max_length=200, verbose_name=u'用户评论')
    add_time = models.DateTimeField(auto_now=True, verbose_name=u'评论添加时间')

    class Meta:
        verbose_name = u'课程评论'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return '{0} -> {1} 的评论'.format(self.user.username, self.course.name)


class UserFavorite(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u'用户')
    # course = models.ForeignKey(Course, verbose_name=u'课程')
    # teacher = models.ForeignKey(Teacher, verbose_name=u'讲师')
    # org = models.ForeignKey(CourseOrg, verbose_name=u'机构')
    # fav_type =
    # 简化 如下：
    fav_id = models.IntegerField(default=0, verbose_name=u'数据id')  # 指明数据表的id
    fav_type = models.IntegerField(choices=((1, "课程"), (2, "课程机构"), (3, "讲师")),
                                   default=1, verbose_name=u'收藏类型')
    add_time = models.DateField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'用户收藏'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return '新用户收藏：'+self.user.nick_name


class UserMessage(models.Model):
    # 这里user不用外键，是因为有2种消息，一种是定向发给某个用户，另一种是发给所有用户的。
    # 所以这里，default = 0代表发给全部用户
    # 不为0，就代表用户id
    # 疑问，不用外键的话，如何和user表关联？？
    user = models.IntegerField(default=0, verbose_name=u'用户id')
    message = models.CharField(max_length=500, verbose_name=u'消息内容')
    has_read = models.BooleanField(default=False, verbose_name=u'是否已读')
    send_time = models.DateTimeField(auto_now=True, verbose_name=u'发送时间')
    add_time = models.DateField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'用户消息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return '用户{0}新消息'.format(self.user)


class UserCourse(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u'用户')
    course = models.ForeignKey(Course, verbose_name=u'课程')
    add_time = models.DateField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'用户学习的课程'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return '{0} -> {1}'.format(self.user.username, self.course.name)
