from django.contrib.auth.models import User
from django.core.serializers import serialize
from django.shortcuts import render, HttpResponse
from article.models import Article
from classifications.models import Classifications
import json
from .forms import ArticleForm
# Create your views here.
import json
from pathlib import Path
import datetime

BASE_DIR = Path(__file__).resolve().parent.parent

def article_filter(data,status):
    return data['temp'] == status

def article_list(request):
    temp_request =int( request.GET.get("temp"))
    article_list = []
    # 取出所有的文章
    articles = Article.objects.all()
    # 将articels对象序列化成json对象
    articles_str = serialize('json', articles)
    articles_json = json.loads(articles_str)
    if temp_request == 0:
        new_articles_json = list (filter(lambda x: x["fields"]['temp'] == 0,articles_json))
    else:
        new_articles_json = list(filter(lambda x: x["fields"]['temp'] == 1, articles_json))
    for article in new_articles_json:
        article_obj = {}
        id = article['pk']
        title = article['fields']['title']
        body = article['fields']['body']
        created = article['fields']['created']
        hot = article['fields']['hot']
        classifications_id = article['fields']['classifications']
        if classifications_id != None:
            classifications = Classifications.objects.get(id=classifications_id)
            article_obj['classifications'] = classifications.title
        else:
            article_obj['classifications'] = None
        article_obj['id'] = id
        article_obj['title'] = title
        article_obj['body'] = body
        article_obj['created'] = created
        article_obj['hot'] = hot
        article_list.append(article_obj)
    return HttpResponse(json.dumps({"code": 200, "data": sorted(article_list, key=lambda x: x['id'])}))


def article_create(request):
    # 添加文章，需要关注添加的是草稿还是文章
    if request.method == "POST":
        # 将表单中的数据赋值到表单实例中
        article_form = ArticleForm(data=request.POST)
        # 判断提交的数据是否满足模型的要求
        if article_form.is_valid():
            # 保存数据，但暂时不提交到数据库
            new_article = article_form.save(commit=False)
            classifications = request.POST['class']
            temp = request.POST['temp']
            class_obj = Classifications.objects.get(title=classifications)
            # 指定数据中的作者id为1
            new_article.author = User.objects.get(id=1)
            new_article.classifications = Classifications.objects.get(title=classifications)
            if int(temp) == 0:
                # 创建非草稿文档
                new_article.temp = 0
                new_article.created = datetime.datetime.now()
                new_article.updated = datetime.datetime.now()
            else:
                # 创建草稿文档
                new_article.temp = 1
                new_article.created = datetime.datetime.now()
                new_article.updated = datetime.datetime.now()
            # 将文章保存到数据库中
            new_article.save()
            return HttpResponse("文章创建成功")
        else:
            # 如果数据不合法，则返回错误信息
            return HttpResponse("表单内容有误，请重新填写")

def article_delete(request, id):
    # 删除文章
    if request.method == "POST":
        # 根据删除的id得到文章对象
        article_obj = Article.objects.get(id=id)
        # 将该文章的delete状态置为True
        article_obj.deleted = True
        article_obj.save()
        return HttpResponse("文章删除成功")


def article_update(request, id):
    # 更新文章的时候需要定义更新的是草稿还是文章
    if request.method == "POST":
        article_form = ArticleForm(data=request.POST)
        if article_form.is_valid():
            article_obj = Article.objects.get(id=id)
            article_obj.title = request.POST['title']
            article_obj.body = request.POST['body']
            temp = request.POST['temp']
            if int(temp) == 0:
                article_obj.temp = 0
                article_obj.updated = datetime.datetime.now()
            else:
                article_obj.temp = 1
                article_obj.updated = datetime.datetime.now()
            article_obj.save()
            return HttpResponse("文章更新成功")
        else:
            return HttpResponse("文章更新失败，内容错误")


def updatehot(request, id):
    if request.method == "GET":
        article_obj = Article.objects.get(id=id)
        article_obj.hot += 1
        article_obj.save()
        return HttpResponse(json.dumps({"code": 200, "message": "OK"}))

def upload_picture(request):
    img = request.FILES.get('img')
    img_name=img.name
    # 文件保存路径
    path=f"{BASE_DIR}/static/{img_name}"
    return_path=f"http://127.0.0.1:8000/articles/get_file?picture={img_name}"
    with open(path,'ab') as fp:
        for chunk in img.chunks():
            fp.write(chunk)
    return HttpResponse(json.dumps({"code":200,"data":return_path}))

def get_file(request):
    file_name=request.GET.get('picture')
    path = f'{BASE_DIR}/static/{file_name}'
    file = open(path,'rb')
    return HttpResponse(file.read(), content_type='image/jpg')

