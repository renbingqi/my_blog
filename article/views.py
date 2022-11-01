from django.shortcuts import render,HttpResponse
from article.models import Article
# Create your views here.
def article_list(request):
    #取出所有的文章
    articles=Article.objects.all()
    for article_obj in articles:
        print(article_obj.title)
        print(article_obj.body)
    return HttpResponse("Hello World")