# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime
from django.db import models
from DjangoUeditor.models import UEditorField

from organization.models import CourseOrg, Teacher


# Create your models here.


class Course(models.Model):
    course_org = models.ForeignKey(CourseOrg, verbose_name=u'所属课程机构', null=True, blank=True)
    teacher = models.ForeignKey(Teacher, verbose_name=u'所属讲师', null=True, blank=True)
    name = models.CharField(max_length=50, verbose_name=u"课程名称")
    desc = models.CharField(max_length=300, verbose_name=u"课程描述")
    detail = UEditorField(verbose_name=u"课程详情", width=600, height=300, imagePath="course/ueditor/",
                          filePath="course/ueditor/",
                          upload_settings={"imageMaxSize": 1204000}, blank=True, default='')
    degree = models.CharField(choices=(('LV1', '初级'), ('LV2', '中级'), ('lv3', '高级')),
                              max_length=3, verbose_name=u'难度')
    learn_times = models.IntegerField(default=0, verbose_name=u"课程时间(分钟)")
    lessen_num = models.IntegerField(default=0, verbose_name=u"章节数")
    course_type = models.CharField(max_length=50, verbose_name=u"课程类别")
    # student_num = models.IntegerField(default=0, verbose_name=u'学习人数')
    favourite_mun = models.IntegerField(default=0, verbose_name=u'收藏人数')
    tag = models.CharField(default='', verbose_name=u'课程标签', max_length=10)
    image = models.ImageField(upload_to="courses/%Y/%m", verbose_name=u"封面图", max_length=150,
                              default='/images/course/default.png')
    click_num = models.IntegerField(default=0, verbose_name=u"课程点击数")
    add_time = models.DateField(default=datetime.now, verbose_name=u"课程添加时间")

    class Meta:
        verbose_name = u"课程"
        verbose_name_plural = verbose_name

    def get_learn_user(self):
        return self.usercourse_set.all()[:5]

    def __unicode__(self):
        return self.name


class Lesson(models.Model):
    course = models.ForeignKey(Course, verbose_name=u"所在课程")
    name = models.CharField(max_length=50, verbose_name=u'章节名')
    add_time = models.DateField(default=datetime.now, verbose_name=u"章节添加时间")

    class Meta:
        verbose_name = u'章节名'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Video(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name=u'所在章节')
    name = models.CharField(max_length=50, verbose_name=u'视频名')
    learn_times = models.IntegerField(default=0, verbose_name=u"课程时间(分钟)")
    add_time = models.DateField(default=datetime.now, verbose_name=u"视频添加时间")

    class Meta:
        verbose_name = u'视频名称'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name=u'所在课程')
    name = models.CharField(max_length=50, verbose_name=u'课程资源名')
    download = models.FileField(upload_to="courses/resource/%Y%m", verbose_name=u'下载地址')
    add_time = models.DateField(default=datetime.now, verbose_name=u"课程资源添加时间")

    class Meta:
        verbose_name = u'课程资源'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name
