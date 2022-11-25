from django.shortcuts import render,HttpResponse
from classifications.models import Classifications
from .forms import ClassificationForm
from article.models import Article
# Create your views here.

def classification_list(request):
    #取出所有的专栏
    classifications=Classifications.objects.all()
    for classification_obj in classifications:
        print(classification_obj.title)
    return HttpResponse("Hello World")


def classification_create(request):
    #添加文章
    if request.method == "POST":
        #将表单中的数据赋值到表单实例中
        classification_form=ClassificationForm(data=request.POST)
        #判断提交的数据是否满足模型的要求
        if classification_form.is_valid():
            #保存数据，但暂时不提交到数据库
            new_classification=classification_form.save(commit=False)
            #将文章保存到数据库中
            new_classification.save()
            return HttpResponse("专栏创建成功。")
        else:
            #如果数据不合法，则返回错误信息
            return HttpResponse("表单内容有误，请重新填写。")


def classification_delete(request,id):
    #删除专栏,专栏删除后需要将所有属于该专栏的文章状态置位删除
    if request.method == "POST":
        #根据删除的id得到专栏对象
        classification_obj = Classifications.objects.get(id=id)
        #将该文章的delete状态置为True
        classification_obj.deleted=True
        article_objs= Article.objects.all()
        classification_obj.save()
        for article_obj in article_objs:
            if article_obj.classifications_id == id:
                article_obj.deleted = 1
            article_obj.deleted=True
            article_obj.save()
        return HttpResponse("专栏删除成功。")

def classification_update(request,id):
    if request.method == "POST":
        classification_form = ClassificationForm(data=request.POST)
        if classification_form.is_valid():
            classification_obj=Classifications.objects.get(id=id)
            classification_obj.title=request.POST['title']
            classification_obj.save()
            return HttpResponse("专栏更新成功。")
        else:
            return HttpResponse("专栏更新失败，内容错误。")