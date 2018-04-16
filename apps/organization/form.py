# _*_ coding:utf-8 _*_

__author__ = 'kevin'
__date__ = '2018/4/16 16:57'
from django import forms

from operation.models import UserAsk


class UserAskForm(forms.ModelForm):
    # 自定义字段
    # other_name = forms.CharField(required=True,max_length=20)
    class Meta:
        model = UserAsk
        fields = ['name', 'mobile', 'course_name']