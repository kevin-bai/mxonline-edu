# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-04-17 14:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0004_auto_20180416_1636'),
        ('courses', '0002_auto_20180328_1255'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_org',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organization.CourseOrg', verbose_name='\u8bfe\u7a0b\u673a\u6784'),
        ),
    ]
