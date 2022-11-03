from django.contrib.auth.models import User
from django.shortcuts import render,HttpResponse
from article.models import Article
import json
from .forms import ArticleForm
# Create your views here.
def article_list(request):
    #取出所有的文章
    articles=Article.objects.all()
    for article_obj in articles:
        print(json.dumps(article_obj))
    return HttpResponse("Hello World")


def article_create(request):
    if request.method == "POST":
        #将表单中的数据赋值到表单实例中
        article_form=ArticleForm(data=request.POST)
        #判断提交的数据是否满足模型的要求
        if article_form.is_valid():
            #保存数据，但暂时不提交到数据库
            new_article=article_form.save(commit=False)
            #指定数据中的作者id为1
            new_article.author=User.objects.get(id=1)
            #将文章保存到数据库中
            new_article.save()
        else:
            #如果数据不合法，则返回错误信息
            return HttpResponse("表单内容有误，请重新填写。")