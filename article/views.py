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
        print(article_obj.body)
    return HttpResponse("Hello World")


def article_create(request):
    #添加文章
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
            return HttpResponse("文章创建成功。")
        else:
            #如果数据不合法，则返回错误信息
            return HttpResponse("表单内容有误，请重新填写。")


def article_delete(request,id):
    #删除文章
    if request.method == "POST":
        #根据删除的id得到文章对象
        article_obj = Article.objects.get(id=id)
        #将该文章的delete状态置为True
        article_obj.deleted=True
        article_obj.save()
        return HttpResponse("文章删除成功。")

def article_update(request,id):
    if request.method == "POST":
        article_form = ArticleForm(data=request.POST)
        if article_form.is_valid():
            article_obj=Article.objects.get(id=id)
            article_obj.title=request.POST['title']
            article_obj.body=request.POST['body']
            article_obj.save()
            return HttpResponse("文章更新成功。")
        else:
            return HttpResponse("文章更新失败，内容错误。")
