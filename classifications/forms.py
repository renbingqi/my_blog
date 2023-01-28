# -*- ecoding: utf-8 -*-
# @ModuleName: forms
# @Author: Rex
# @Time: 2022/11/3 7:41 下午

from django import forms
from .models import Classifications
#专栏的表单类
class ClassificationForm(forms.ModelForm):
    class Meta:
        #指明数据来源
        model=Classifications
        # 定义表单包含的字段
        fields=['title']

