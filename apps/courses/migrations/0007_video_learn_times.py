# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-04-19 16:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_remove_course_student_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='learn_times',
            field=models.IntegerField(default=0, verbose_name='\u8bfe\u7a0b\u65f6\u95f4(\u5206\u949f)'),
        ),
    ]
