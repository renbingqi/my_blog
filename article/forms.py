# -*- ecoding: utf-8 -*-
# @ModuleName: forms
# @Author: Rex
# @Time: 2022/11/3 7:41 下午

from django import forms
from .models import Article
#写文章的表单类
class ArticleForm(forms.ModelForm):
    class Meta:
        #指明数据来源
        model=Article
        # 定义表单包含的字段
        fields=('title','body')

