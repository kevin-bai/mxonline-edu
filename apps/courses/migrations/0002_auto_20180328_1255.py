# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-28 12:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='degree',
            field=models.CharField(choices=[('LV1', '\u521d\u7ea7'), ('LV2', '\u4e2d\u7ea7'), ('lv3', '\u9ad8\u7ea7')], max_length=3, verbose_name='\u96be\u5ea6'),
        ),
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(default='/images/course/default.png', max_length=150, upload_to='courses/%Y/%m', verbose_name='\u5c01\u9762\u56fe'),
        ),
    ]
