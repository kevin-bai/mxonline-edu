# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-28 11:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseorg',
            name='image',
            field=models.ImageField(default='images/default.png', upload_to='courseOrg/%Y%m', verbose_name='\u8bfe\u7a0b\u56fe\u7247'),
        ),
    ]
