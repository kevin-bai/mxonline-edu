# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-04-16 16:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0003_courseorg_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseorg',
            name='course_num',
            field=models.IntegerField(default=0, verbose_name='\u8bfe\u7a0b\u6570\u91cf'),
        ),
        migrations.AddField(
            model_name='courseorg',
            name='students_num',
            field=models.IntegerField(default=0, verbose_name='\u5b66\u4e60\u4eba\u6570'),
        ),
        migrations.AlterField(
            model_name='courseorg',
            name='category',
            field=models.CharField(choices=[('org', '\u57f9\u8bad\u673a\u6784'), ('person', '\u4e2a\u4eba'), ('college', '\u9ad8\u6821')], default='org', max_length=20, verbose_name='\u8bfe\u7a0b\u7c7b\u522b'),
        ),
    ]