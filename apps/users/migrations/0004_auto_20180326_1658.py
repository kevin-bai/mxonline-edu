# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-26 16:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20180326_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('mail', '\u7537'), ('female', '\u5973')], max_length=6, verbose_name='\u6027\u522b'),
        ),
    ]
