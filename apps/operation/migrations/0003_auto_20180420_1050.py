# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-04-20 10:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0002_auto_20180417_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursecomments',
            name='add_time',
            field=models.DateTimeField(auto_now=True, verbose_name='\u8bc4\u8bba\u6dfb\u52a0\u65f6\u95f4'),
        ),
    ]
