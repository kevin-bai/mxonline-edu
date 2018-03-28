# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime

from django.db import models

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name=u"课程名称")
    desc = models.CharField(max_length=300, verbose_name=u"课程描述")
    detail = models.TextField(verbose_name=u"课程详情")
    degree = models.CharField(choices=(('LV1', '初级'), ('LV2', '中级'), ('lv3', '高级')),
                              max_length=3, verbose_name=u'难度')
    learn_times = models.IntegerField(default=0, verbose_name=u"课程时间(分钟)")
    lessen_num = models.IntegerField(default=0, verbose_name=u"章节数")
    course_type = models.CharField(max_length=50, verbose_name=u"课程类别")
    student_num = models.IntegerField(default=0, verbose_name=u'学习人数')
    favourite_mun = models.IntegerField(default=0,verbose_name=u'收藏人数')
    image = models.ImageField(upload_to="courses/%Y/%m", verbose_name=u"封面图", max_length=150,
                              default='/images/course/default.png')
    click_num = models.IntegerField(default=0, verbose_name=u"课程点击数")
    add_time = models.DateField(default=datetime.now, verbose_name=u"课程添加时间")

    class Meta:
        verbose_name = u"课程"
        verbose_name_plural = verbose_name


class Lesson(models.Model):
    course = models.ForeignKey(Course, verbose_name=u"所在课程")
    name = models.CharField(max_length=50, verbose_name=u'章节名')
    add_time = models.DateField(default=datetime.now, verbose_name=u"章节添加时间")

    class Meta:
        verbose_name = u'章节名'
        verbose_name_plural = verbose_name


class Video(models  .Model):
    lesson = models.ForeignKey(Lesson, verbose_name=u'所在章节')
    name = models.CharField(max_length=50, verbose_name=u'视频名')
    add_time = models.DateField(default=datetime.now, verbose_name=u"视频添加时间")

    class Meta:
        verbose_name = u'视频名称'
        verbose_name_plural = verbose_name


class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name=u'所在课程')
    name = models.CharField(max_length=50, verbose_name=u'课程资源名')
    download = models.FileField(upload_to="courses/resource/%Y%m", verbose_name=u'下载地址')
    add_time = models.DateField(default=datetime.now, verbose_name=u"课程资源添加时间")

    class Meta:
        verbose_name = u'课程资源'
        verbose_name_plural = verbose_name
