# _*_ coding:utf-8 _*_

__author__ = 'kevin'
__date__ = '2018/3/29 14:26'

from django import forms


class LoginForm(forms.Form):
    # 这个变量名必须和form表单中提交的name一致
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)
