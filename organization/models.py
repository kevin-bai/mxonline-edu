# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime

from django.db import models

# Create your models here.


class CityDict(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'城市名字')
    desc = models.CharField(max_length=200, verbose_name=u'城市描述')
    add_time = models.DateField(default=datetime.now, verbose_name=u'城市加入时间')

    class Meta:
        verbose_name = u'城市'
        verbose_name_plural = verbose_name


class CourseOrg(models.Model):
    city = models.ForeignKey(CityDict, verbose_name=u'所在城市')
    name = models.CharField(max_length=50, verbose_name=u'机构名称')
    desc = models.TextField(verbose_name=u'机构描述')
    click_num = models.IntegerField(default=0, verbose_name=u'点击数')
    favorite_num = models.IntegerField(default=0, verbose_name=u'收藏数')
    image = models.ImageField(upload_to='courseOrg/%Y%m', verbose_name=u'课程图片')
    address = models.CharField(max_length=150, verbose_name=u'机构地址')
    add_time = models.DateField(default=datetime.now, verbose_name=u'机构加入时间')

    class Meta:
        verbose_name = u'课程机构'
        verbose_name_plural = verbose_name


class Teacher(models.Model):
    org = models.ForeignKey(CourseOrg, verbose_name=u'所在机构')
    name = models.CharField(max_length=50, verbose_name=u'教师名字')
    work_years = models.IntegerField(verbose_name=u'工作年限')
    work_company = models.CharField(max_length=50, verbose_name=u'就职公司')
    work_position = models.CharField(max_length=50, verbose_name=u'工作职位')
    points = models.CharField(max_length=50, verbose_name=u'教学特点')
    click_num = models.IntegerField(default=0, verbose_name=u'点击数')
    favorite_num = models.IntegerField(default=0, verbose_name=u'收藏数')
    add_time = models.DateField(default=datetime.now, verbose_name=u'教师加入时间')

    class Meta:
        verbose_name = u'教师'
        verbose_name_plural = verbose_name

