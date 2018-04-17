# _*_ coding:utf-8 _*_
import re

__author__ = 'kevin'
__date__ = '2018/4/16 16:57'
from django import forms

from operation.models import UserAsk, UserFavorite


class UserAskForm(forms.ModelForm):
    # 自定义字段
    # other_name = forms.CharField(required=True,max_length=20)
    class Meta:
        model = UserAsk
        fields = ['name', 'mobile', 'course_name']

    def clean_mobile(self):
        """
        验证手机号码是否合法
        :return:
        """
        mobile = self.cleaned_data['mobile']
        mobile_reg = '^1([358][0-9]|4[579]|66|7[0135678]|9[89])[0-9]{8}$'
        p = re.compile(mobile_reg)
        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError(u"手机号码异常", code='mobile_invalid')


class UserFavoriteForm(forms.ModelForm):
    class Meta:
        model = UserFavorite
        fields = ['user', 'fav_id', 'fav_type']
